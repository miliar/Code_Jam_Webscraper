#include <iostream>
#include <cstdlib>
using namespace std;
#define LEFT(i) i<<1
#define RIGHT(i) (i<<1)+1
#define ulint unsigned long int

typedef struct node
{
	unsigned long int index;
	unsigned long int l;
	unsigned long int r;
	unsigned long int min;
	unsigned long int max;
}node;

void MaxHeapify(node arr[], ulint i, ulint heap_size)
{
	ulint largest=i;
	ulint left=LEFT(i);
	ulint right=RIGHT(i);
	if(left<=heap_size)
	{
		if(arr[largest-1].min<arr[left-1].min)
			largest=left;
		if(arr[largest-1].min==arr[left-1].min)
		{
			if(arr[largest-1].max<arr[left-1].max)
				largest=left;
			if(arr[largest-1].max==arr[left-1].max && arr[left-1].index<arr[largest-1].index)
				largest=left;
		}
	}
	if(right<=heap_size)
	{
		if(arr[largest-1].min<arr[right-1].min)
			largest=right;
		if(arr[largest-1].min==arr[right-1].min)
		{
			if(arr[largest-1].max<arr[right-1].max)
				largest=right;
			if(arr[largest-1].max==arr[right-1].max && arr[right-1].index<arr[largest-1].index)
				largest=right;
		}
	}
	if(largest!=i)
	{
		swap(arr[largest-1],arr[i-1]);
		MaxHeapify(arr,largest,heap_size);
	}
}

void ExtractMax(node arr[], ulint &heap_size)
{
	swap(arr[0],arr[heap_size-1]);
	heap_size--;
	MaxHeapify(arr,1,heap_size);
}

void BuildHeap(node arr[], ulint heap_size)
{
	for(ulint i=heap_size/2; i>0; i--)
		MaxHeapify(arr,i,heap_size);
}

ulint min(ulint a, ulint b)
{
	return a<b?a:b;
}

ulint max(ulint a, ulint b)
{
	return a>b?a:b;
}

int main()
{
	unsigned long int t,t1,n,k,i;
	cin>>t;
	t1=1;
	while(t--)
	{
		cin>>n>>k;
		if(n==k)
		{
			cout<<"Case #"<<(t1)++<<": 0 0"<<endl;
			continue;
		}
		node arr[n];
		for(i=0; i<n; i++)
		{
			arr[i].index=i+1;
			arr[i].l=i;
			arr[i].r=n-i-1;
			arr[i].min=min(arr[i].l,arr[i].r);
			arr[i].max=max(arr[i].l,arr[i].r);
		}
		BuildHeap(arr,n);
		ulint heap_size=n;
		ulint j;
		for(i=0; i<k; i++)
		{
			ExtractMax(arr,heap_size);
			for(j=0; j<heap_size; j++)
			{
				if(arr[j].index<arr[heap_size].index && arr[j].index>=arr[heap_size].index-arr[heap_size].l)
					arr[j].r=arr[j].r-arr[heap_size].r-1;
				if(arr[j].index>arr[heap_size].index && arr[j].index<=arr[heap_size].index+arr[heap_size].r)
					arr[j].l=arr[j].l-arr[heap_size].l-1;
				arr[j].min=min(arr[j].l,arr[j].r);
				arr[j].max=max(arr[j].l,arr[j].r);
			}
			BuildHeap(arr,heap_size);
		}
		cout<<"Case #"<<(t1)++<<": "<<max(arr[heap_size].l,arr[heap_size].r)<<" "<<min(arr[heap_size].l,arr[heap_size].r)<<endl;
	}
	return 0;
}
