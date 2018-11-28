#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <math.h>
#include <stdio.h>

#define ifn(x) if(!(x))

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int I=1;I<=T;I++)
	{
		cout << "Case #" << I << ": ";
		int n,p;
		cin >> n >> p;
		vector<int> v(n);
		for(int i=0;i<n;i++)
			cin >> v[i],v[i] = v[i]%p;
		vector<int> freq(p);
		for(int i=0;i<n;i++)
			freq[v[i]]++;
		int res = 0;
		res+=freq[0];
		freq[0]=0;
		if(p<4)
		{
			ifn(p%2) {
				res+=freq[p/2]/2;
				freq[p/2] = freq[p/2]%2;
			}
			for(int i=1;i<(p+1)/2;i++)
			{
				int asdf=min(freq[i],freq[p-i]);
				res+=asdf;
				freq[i]-=asdf;
				freq[p-i]-=asdf;
			}
			for(int i=1;i<p;i++)
			{
				int a=1;
				int k=i;
				while(k%p)
					a++,k+=i;
				//cout << a << endl;
				res+=freq[i]/a+!!(freq[i]%a);
			}
		}
		else// p=4. Combinaciones: 112,22,13,31,1111,3333,332,123
		// si tenemos 3333221, lo mejor es 13, 22, 333; 332,123,3
		{
			ifn(p%2) {
				res+=freq[p/2]/2;
				freq[p/2] = freq[p/2]%2;
			}
			for(int i=1;i<(p+1)/2;i++)
			{
				int asdf=min(freq[i],freq[p-i]);
				res+=asdf;
				freq[i]-=asdf;
				freq[p-i]-=asdf;
			}
			//cout << res;
			while(freq[1]>1 && freq[2])
				res++,freq[1]-=2,freq[2]--;
			//	cout << res;
			while(freq[3]>1 && freq[2])
				res++,freq[3]-=2,freq[2]--;
			//	cout << res;
			while(freq[1] && freq[2] && freq[3])
				res++,freq[1]--,freq[2]--,freq[3]--;
			while(freq[1]>3)
				res++,freq[1]-=4;
			while(freq[3]>3)
				res++,freq[3]-=4;
			
			for(int i=1;i<p;i++)
			{
				if(freq[i]){
					res++;
					break;
				}
			}
		}
		cout << res << endl;
	}
}
