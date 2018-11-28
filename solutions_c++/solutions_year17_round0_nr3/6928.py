#include <iostream>
using namespace std ;
#define MAXN 1000000

#define MIN(A,B) A < B? A:B
#define MAX(A,B) A > B? A:B

struct ndata{
unsigned long long ls ;
unsigned long long rs ;
unsigned long long s ;
bool bOccupied ;
};

typedef unsigned long long ull ;
ndata *input[MAXN];

void UpdateRange(ull i ,ndata *parr[], ull N);
//if it returns true then prefer a else b
bool compndata(ndata *a , ndata *b )
{
	ull amin = MIN(a->ls,a->rs), bmin = MIN(b->ls, b->rs);
	if( amin != bmin)
		return amin > bmin ;
	ull amax = MAX(a->ls,a->rs) , bmax = MAX(b->ls, b->rs);
	if( amax != bmax)
		return amax > bmax ;
	return a->s < b->s ;
}

class MaxHeap{

public:

MaxHeap(ndata *arr[], long long N):size(N)
{
	for(long long i = 0 ; i < N ;++i)
	{
		data[i] = arr[i] ;
	}
	last = N - 1 ;
	BuildHeap();
}
~MaxHeap()
{
}

//void Insert(int key);
ndata* ExtractMax() ;


private:
long long Parent(long long i) { return (i-1)/2 ; }
void Heapify(long long i );
//void DecreaseKey();
void BuildHeap();

ndata *data[MAXN];
long long last ;
long long size ;
};

void MaxHeap::Heapify(long long i)
{
	long long largest = i ;
	long long l = 2*i + 1 ;
	long long r = 2*i + 2 ;
	if( l <= last && compndata(data[l],data[largest] ) )
	{
		largest = l ;
	}
	if( r <= last && compndata(data[r],data[largest] ))
	{
		largest = r ;
	}
	if( largest != i)
	{
		ndata* temp = data[i] ;
		data[i] = data[largest];
		data[largest] = temp ;
		Heapify(largest);
	}
	
}

void MaxHeap::BuildHeap()
{
	for( long long i = Parent(last) ; i >= 0;--i)
	{
		Heapify(i);
	}
}



ndata* MaxHeap::ExtractMax()
{
	ndata* max = data[0] ;
	data[0] = data[last];
	--last ;
	//To do update range before heapify
	UpdateRange(max->s ,input, size);
	BuildHeap();
	//Heapify(0) ;
	return max ;
}

void UpdateRange(ull i ,ndata *parr[], ull N)
{
	ull l = i , r = i ;
		
	while( !(parr[l]->bOccupied && parr[r]->bOccupied) )
	{
		if( l > 0 && !parr[l]->bOccupied)
		{			
			--l ;
			parr[l]->rs = i - l - 1 ;
		}
		if( r < N - 1 && !parr[r]->bOccupied){
			++r ;
			parr[r]->ls = r - i - 1 ;
			}
					
		if((l == 0 || parr[l]->bOccupied) && (r == (N-1) || parr[r]->bOccupied) )
			break ;
	}
	parr[i]->bOccupied = true ;
}

int main()
{
	int T ;	
	cin >> T ;
	ull N , K ;
	for(int j = 1 ; j <= T ;++j)
	{
		cin >> N >> K ;
		for(long long i = 0 ; i < N ;++i)
		{
			input[i] = new ndata();
			input[i]->ls = i ;
			input[i]->rs = N - 1 - i ;
			input[i]->s = i ;
			input[i]->bOccupied = false ;
		}
		MaxHeap mh(input,N);
		ndata* last ;
		for(ull ik = 0; ik < K ;++ ik)
		{
			last = mh.ExtractMax() ;
			//cout << last->s << endl;
		}
		ull xv = MAX(last->ls,last->rs) ;
		ull xn = MIN(last->ls,last->rs) ;
		cout << "Case #" << j << ": " << xv << " " << xn << endl ;
	}
	return 0 ;
}

