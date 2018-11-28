#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <memory.h>
#include <sstream>
#include <deque>
const int pi=acos(-1);
typedef long long ll;
using namespace std;
int t,j;
char temp[1069];
int main(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	cin>>t;
	while(t--)
	{
		bool f=0;
		int k,n,ans=0;
		string s;
		scanf("%s %d",temp,&k);
		s=temp;
		n=s.size();
		for(int i=0;i<n-k+1;i++)
			if(s[i]=='-')
			{
				ans++;
				for(int lel=i;lel<i+k;lel++)
					if(s[lel]=='-')
						s[lel]='+';
					else
						s[lel]='-';
			}
		for(int i=0;i<n;i++)
			if(s[i]=='-')
				f=1;
		if(f)
			cout<<"Case #"<<++j<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<++j<<": "<<ans<<endl;		
	}
	return 0;
}