// Courtesy of https://www.techiedelight.com/hybrid-quicksort/

#include <iostream>
using namespace std;

// Number of elements to be sorted
#define N 1000000

// Number of sorting runs
#define NUM 10

// perform insertion sort on arr[]
void insertionSort(int arr[], int low, int n)
{
	// Start from second element (element at index 0
	// is already sorted)
	for (int i = low + 1; i <= n; i++)
	{
		int value = arr[i];
		int j = i;

		// Find the index j within the sorted subset arr[0..i-1]
		// where element arr[i] belongs
		while (j > low && arr[j - 1] > value)
		{
			arr[j] = arr[j - 1];
			j--;
		}
		// Note that subarray arr[j..i-1] is shifted to
		// the right by one position i.e. arr[j+1..i]

		arr[j] = value;
	}
}

int Partition (int a[], int low, int high)
{
	// Pick rightmost element as pivot from the array
	int pivot = a[high];

	// elements less than pivot will be pushed to the left of pIndex
	// elements more than pivot will be pushed to the right of pIndex
	// equal elements can go either way
	int pIndex = low;

	// each time we finds an element less than or equal to pivot, pIndex
	// is incremented and that element would be placed before the pivot.
	for (int i = low; i < high; i++)
	{
		if (a[i] <= pivot)
		{
			swap(a[i], a[pIndex]);
			pIndex++;
		}
	}
	// swap pIndex with Pivot
	swap (a[pIndex], a[high]);

	// return pIndex (index of pivot element)
	return pIndex;
}

void optimizedQuickSort(int A[], int low, int high, int k)
{
	while (low < high)
	{
		// do insertion sort if k or smaller
		if (high - low < k)
		{
			insertionSort(A, low, high);
			break;
		}
		else
		{
			int pivot = Partition(A, low, high);

			// tail call optimizations - recur on smaller sub-array
			if (pivot - low < high - pivot) {
				optimizedQuickSort(A, low, pivot - 1, k);
				low = pivot + 1;
			} else {
				optimizedQuickSort(A, pivot + 1, high, k);
				high = pivot - 1;
			}
		}
	}
}

int main()
{
	int arr[N], dup[N];

	// seed for random input
	srand(time(NULL));

	// to measure time taken by optimized and non-optimized Quicksort
	clock_t begin, end;
	double t1 = 0.0, t2 = 0.0;

	// perform Quicksort NUM times and take average
	for (int i = 0; i < NUM; i++)
	{
		// generate random input
		for (int i = 0; i < N; i++)
			dup[i] = arr[i] = rand() % 10;

		// Perform Optimized Quicksort on dup[]
		begin = clock();
		optimizedQuickSort(dup, 0, N-1, 10000);
		end = clock();

		// calculate time taken by optimized QuickSort
		cout << endl << (double)(end - begin)/CLOCKS_PER_SEC << endl;
		t2 += (double)(end - begin) / CLOCKS_PER_SEC;

	}

	cout << "\nAverage time taken by Optimized Quicksort: " << t2/NUM << endl;

	return 0;
}