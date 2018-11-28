#include<bits/stdc++.h>
using namespace std;


#define MAX 1005

#define f(i, a, b) for(int i=a; i<=b; i++)


typedef bitset<MAX> bit;
bit flip[2017]; int tam;


int main()
{
	int T, k, s;
	scanf("%d ", &T);

	f(t, 1, T)
	{
		bit original= bit(0);
		
		s=0;tam =0;
		char c;
		for(; ; )
		{
			scanf("%c", &c);
			
			if(c==' ')
				break;
			if(c=='-') /// QUERO DEIXAR TUDO 0
			{	
				original[s]=1;
			}			
			s++;
			
		}
		scanf("%d ", &k);

		bit bitmask = original;
		int n1=0;
		for(int i=0; i<s; i++)
		{
			if(bitmask[i]==1 && i+k-1<s)
			{
				n1++;
				for(int j=i; j<=i+k-1; j++)
					bitmask[j]= 1-bitmask[j];
			}

		}

		for(int i=s-1; i>=max(s-1-(k-1),0); i--){
			if(bitmask[i])
			{
				n1 = -1;
				break;
			}
		}

		for(int i=0; i<s; i++)
			bitmask[i] = original[s-1-i];

		int n2=0;
		for(int i=0; i<s; i++)
		{
			if(bitmask[i]==1 && i+k-1<s)
			{
				n2++;
				for(int j=i; j<=i+k-1; j++)
					bitmask[j]= 1-bitmask[j];
			}

		}
		
		for(int i=s-1; i>=max(s-1-(k-1),0); i--){
			if(bitmask[i])
			{
				n2 = -1;
				break;
			}
		}

		if(n1==-1 && n2==-1)
			cout<<"Case #"<<t<<": IMPOSSIBLE"<<	endl;	
		else
			cout<<"Case #"<<t<<": "<<min(n1, n2)<<endl;



		// for(int i=1; i<=tam; i++)
		// {
		//  	cout<<flip[i]<<endl;
		//  }

		// cout<<bitmask<<endl;
		// cout<<k<<endl<<endl;
	}

	
	return 0;
}	