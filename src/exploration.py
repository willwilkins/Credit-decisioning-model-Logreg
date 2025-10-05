import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df, columns):
    """Plot distribution of specified columns."""
    fig, axes = plt.subplots(len(columns), 1, figsize=(10, 4*len(columns)))
    for i, col in enumerate(columns):
        df[col].hist(ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    return fig

def plot_correlation_matrix(df):
    """Plot correlation heatmap."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    return plt.gcf()


def univariate_multiplotter(features, numeric_cols, categorical_cols, name=None):
    """ Plots subplots, histograms or count plots for numeric and categorical columns respectively."""
    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Create a figure with subplots
    assert len(numeric_cols) + len(categorical_cols) <= len(features.columns), "Too many columns to plot. Limit to 20."
    fig, axes = plt.subplots(nrows=4, ncols=5, figsize=(35, 25))
    # Flatten the axes array for easy iteration
    axes = axes.flatten()

    # Create a clone dataframe and then sort categorical and binary columns before plotting
    # Create a clone of the original dataframe
    clone = features.copy()
        
    print('Plot no:')
    no_features = len(clone.columns)

    # Loop through each feature and plot its histogram (for numeric)/countplot (for categorical/binary)
    for i, column in enumerate(clone.columns):
        print(i,'/',no_features)
        if column in numeric_features:
            # Plot the histogram
            sns.histplot(clone[column], bins=30, kde=True, ax=axes[i])
            # Set the title and labels
            axes[i].set_title(f'Histogram of {column}')
        elif column in categorical_features:
            # Sort the values in descending order
            clone[column] = pd.Categorical(clone[column], categories=clone[column].value_counts().index, ordered=True)
            # Plot the countplot
            sns.countplot(x=clone[column], ax=axes[i])
            # Set the title and labels
            axes[i].set_title(f'Countplot of {column}')
        # Set the title and labels
        axes[i].set_xlabel(column)
        axes[i].set_ylabel('Frequency')
        fig.tight_layout()
    # Show the plot
    fig.suptitle(name, fontsize=40)
    fig.subplots_adjust(top=0.9)  # Adjust the top to make room for the title
    fig.show()

    return fig