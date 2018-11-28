#include <iostream>
#include <vector>

using namespace std;

struct TreeNum
{
  int value;
  int freq;
};

vector<int>Ans(int N,int K);
vector<int>Gaps(int Kgap);
void GenNext(TreeNum &larger, TreeNum &smaller);
int Max(vector<int>v)
{
	int largest=NULL;
	for (int x: v) if(!largest || x>largest) largest=x;
	return largest;
}

int Min(vector<int>v)
{
	int smallest=NULL;
	for (int x: v) if(!smallest || x<smallest) smallest=x;
	return smallest;
}
		

int main()
{
  int cases;
  cin>>cases;
  for(int c=1; c<=cases; c++)
  {
      int N,K; cin>>N>>K; //N is the number of stalls, K the number of inserts
      vector<int>Answers=Ans(N,K);  
      cout<<"Case #"<<c<<": "<<Answers[0]<<" "<<Answers[1]<<endl; //The left gap and the right gap
  }
}

void GenNext(TreeNum &larger, TreeNum &smaller)
{
			
	//Each will generate kids
	vector<int>smallerKids;
	if(smaller.value%2)
	{
		smallerKids.push_back((smaller.value-1)/2);
		smallerKids.push_back((smaller.value-1)/2);
	}
	else
	{
		smallerKids.push_back(smaller.value/2);
		smallerKids.push_back(smallerKids[0]-1);
	}

	vector<int>largerKids;
	if(larger.value%2)
	{
		largerKids.push_back((larger.value-1)/2);	
		largerKids.push_back((larger.value-1)/2);
	}
	else
	{
		largerKids.push_back(larger.value/2);
		largerKids.push_back(largerKids[0]-1);
	}

	int newSmallerVal=Min(smallerKids);
	if(Min(largerKids)<newSmallerVal) newSmallerVal=Min(largerKids);

	int newLargerVal=Max(smallerKids);

	if(Max(largerKids)>newLargerVal) newLargerVal=Max(largerKids);

	//Now we have the values, we just need their respective frequencies
	//Watch our for larger and smaller being the same	
	TreeNum newLarger, newSmaller;
	newLarger.freq=0; newSmaller.freq=0;
	newLarger.value=newLargerVal; newSmaller.value=newSmallerVal;

	if(larger.value==smaller.value) //Their frequencies will be the same as well
	{
		//If they produced just copies
		if(newLarger.value==newSmaller.value)
		{
			
			newLarger.freq=larger.freq*2;
			newSmaller.freq=larger.freq*2;			
		}
		else
		{
			newLarger.freq=larger.freq;
			newSmaller.freq=larger.freq;
		}
		larger=newLarger; smaller=newSmaller;
		return;
	}

	for(int k : smallerKids)
	{
		if(k==newSmaller.value) { newSmaller.freq+=smaller.freq; }
		else if(k==newLarger.value) { newLarger.freq+=smaller.freq; }
		//It should always meet one of the two conditions
	}

	for(int k : largerKids)
	{
		if(k==newSmaller.value) { newSmaller.freq+=larger.freq; }
		else if(k==newLarger.value) { newLarger.freq+=larger.freq; }		  
	}
	
	larger=newLarger; smaller=newSmaller;
}

vector<int>Gaps(int Kgap)
{
	vector<int>ans;
	if(Kgap%2==1) ans.resize(2,Kgap>>1);
	else
	{	
		ans.push_back(Kgap>>1);
		ans.push_back(ans[0]-1);
	}
	return ans;
}

vector<int>Ans(int N,int K)
{
	//Find the largest x such that 2^x -1 < K
	int Kcopy=K;
	int x=0;
	while (Kcopy!=1)
	{
		Kcopy>>=1;
		x++;
	}
  
	//X is the number of levels we want to go down.
	//At each level there will be two numbers - the larger and the smaller. We want to keep track of them and how many of each there is.
  
	TreeNum larger,smaller;
	larger.value=N; larger.freq=1;
	smaller=larger;
	for(int level=0; level<x; level++) GenNext(larger,smaller);
  
	//Now we're at the level where we'll be making the Kth insert, having just made 2*x -1 inserts.
	//GenNext(larger,smaller); //This will give us the frequencies of each - the rule is to split the larger first
	int largeRange=(1<<x)-1+larger.freq;

	//Then the Kth insert is going into the large gap
	if(K<=largeRange) return Gaps(larger.value);
	else return Gaps(smaller.value);
}
  
	  
	  
	  
		  
  
  
  
