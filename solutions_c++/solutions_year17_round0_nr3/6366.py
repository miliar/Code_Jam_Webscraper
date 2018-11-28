
// just use a heap of pair with size of the index of the gap and the size of the gap to the left as the second parameter(highest gap at the top, for equual gaps lowest index to the left)
#include<iostream> 
#include<queue>
using namespace std;

typedef pair<int, int> PAIR_INTS;
class myComp{
	public:
	bool operator()(PAIR_INTS p1, PAIR_INTS p2)
	{
		
		//first = index of gap start, second = size of gap 
		if(p1.second==p2.second)
			return p1.first>p2.first;
		else
			return p1.second<p2.second;
	}
};

typedef priority_queue< PAIR_INTS, vector< PAIR_INTS >, myComp > PQ;

void divideTheGapAndPrint(int i, PAIR_INTS& pr, PQ& heap)
{
	//pr.first = index of gap start, pr.second = size of gap 
	int idxToFill=pr.first+(pr.second-1)/2;
	//cout<<idxToFill<<",";
	int gap1=idxToFill-(pr.first);
	int gap2=(pr.first+pr.second-1)-(idxToFill);
	
	if(gap1>gap2) 
		cout << "Case #" << i << ": " << gap1<<" "<< gap2 << endl;
	else
		cout << "Case #" << i << ": " << gap2<<" "<< gap1 << endl;
}

void divideTheGapAndFill(PAIR_INTS& pr, PQ& heap)
{
	//pr.first = index of gap start, pr.second = size of gap 
	int idxToFill=pr.first+(pr.second-1)/2;
	//cout<<idxToFill<<",";
	int gap1=idxToFill-(pr.first);
	int gap2=(pr.first+pr.second-1)-(idxToFill);
	if(gap1>0)
		heap.push(make_pair(pr.first, gap1));
	if(gap2>0)
		heap.push(make_pair(idxToFill+1, gap2));
	
}


int main()  
{
	int t, n, k;
	cin>>t;
	for(int i=1; i<=t; ++i)
	{
		cin >> n >>k;
		PQ heap;
		heap.push(make_pair(0, n));
		int count=1; 
		PAIR_INTS lastIdxGaps;
		while(count<k)
		{
				auto pr=heap.top();
				heap.pop();
				divideTheGapAndFill(pr, heap);
				++count;
		}
		auto pr=heap.top();
		divideTheGapAndPrint(i, pr, heap);
		
	}
	return 0;	
}

