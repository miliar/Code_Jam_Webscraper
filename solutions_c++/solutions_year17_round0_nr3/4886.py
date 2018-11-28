#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

struct Pair{
	long long left;
	long long right;
	long long diff;
};

long long findMid(long long left, long long right)
{
	//cout<<"Left = "<<left<<"\t";
	//cout<<"right = "<<right<<"\n";
	long long mid = (right-left)/2;
	return left+mid;
}


void fillDiff(struct Pair *Diff, long long *mid, long long left , long long right)
{
	long long loop=0;
	long long start=-1;
	for(long long i=left; i<right; i++)
	{
		if(start==-1 && mid[i] == 0)
			start=i;
		else if ( mid[i] != 0)
		{
			Diff[loop].left = start;
			Diff[loop].right = i-1;
			Diff[loop++].diff= i-start;
			start=i+1;
		}
	}
	//cout<<"r="<<right<<", l="<<start<<"\n";
	Diff[loop].left = start;
	Diff[loop].right = right-1;
	Diff[loop].diff=right-start;
}


int main()
{
	long long T=0;

	cin>>T;
	for(long long t=1; t<=T; t++)
	{
		long long N,K;

		cin>>N;
		cin>>K;

		cout<<"Case #"<<t<<": ";
		//struct Pair *Diff = new struct Pair[N];
		vector <struct Pair> Diff;
		//vector <long long> midQ;
		priority_queue<long long> midQ;
		long long LS=0;
		long long RS=0;
		bool isDone = false;
		midQ.push(N);

		long long ctr = 1;

		while(!isDone && !midQ.empty())
		{
			//sort(midQ.begin(),midQ.end());

			/*
			for(int i=0; i<midQ.size();i++)
			{
				cout<<"\nVECT = "<<midQ[i];
			}
			*/

			int right = midQ.top();
			midQ.pop();	
			long long mI = right/2;
			//cout<<"\n"<<right<<"::"<<ctr-1<<"\t"<<"MID ="<<mI<<"\t";
			struct Pair tmp;
			if(right % 2 == 0)
			{
				tmp.left = mI;
				tmp.right = mI-1;
			}
			else
			{
				tmp.left = mI;
				tmp.right = mI;
			}

			Diff.push_back(tmp);

			

			if(tmp.left != 0)
				midQ.push(tmp.left);
			if(tmp.right != 0)
				midQ.push(tmp.right);


			//cout<<"midQ = "<<tmp.left<<" : "<<tmp.right<<"\n";

			if(ctr == K)
				isDone = true;
			ctr++;


		}



		/*
		if(K == 1)
		{
			long long mI = findMid(0,N-1);
			LS = mI - 0;
			RS = N-1 - mI;
		}
		else
		{
			for(long long j=0; j<K; j++)
			{
				if( j==0 )
				{
					long long mI = findMid(0,N-1);
					mid[mI]=1;
				}
				else
				{
					long long nextI = 0;
					long long nextMax = Diff[0].diff;

					for(long long i=0; Diff[i].left < 0; i++)
					{
						//cout<<"inside";
						nextI = i+1;
						nextMax = Diff[i+1].diff;
					}

					//cout<<"nextI = "<<nextI<<"\n";

					for(long long i=nextI+1; i < N; i++)
					{
						if(Diff[i].diff > nextMax)// Diff[i-1].diff)
						{
							nextMax = Diff[i].diff;
							nextI = i;
						}
					}
					long long mI = findMid(Diff[nextI].left,Diff[nextI].right);
					LS = mI-Diff[nextI].left;
					RS = Diff[nextI].right-mI;

					//cout<<"MID: "<<mI<<"\n";
					mid[mI]=1;

				}

				
				for(long long a=0; a<N; a++)
					cout<<mid[a];
				cout<<"\n";
				

				fillDiff(Diff,mid,0,N);

			}
		}
		*/
		
		//cout<<"LS = "<<LS<<" : RS = "<<RS<<"\n";
		//
		//cout<<max(LS,RS)<<" "<<min(LS,RS);
		cout<<Diff[K-1].left<<" "<<Diff[K-1].right;
		cout<<"\n";
		

		
	}
	return 0;
}
