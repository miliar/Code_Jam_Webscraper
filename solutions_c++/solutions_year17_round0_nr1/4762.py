#include<bits/stdc++.h>
#define INF LONG_MAX-100
#define for(p,x,y) for(int p=x;p<y;p++)
#define in(a) scanf("%d",&a);
#define INPUT
typedef long long ll;
using namespace std;
int flip(string s,int k)
{
	int l=s.length();
	int c=0;
	int p=(l-k+1);
	for(i,0,p)
	{
		if(s[i]=='-')
		{
			c++;
		for(j,i,(i+k))
		{
			if(s[j]=='-')
			s[j]='+';
			else
			s[j]='-';
		}
	}
}
	for(i,0,l)
	{
		if(s[i]=='-')
		return -1;
	}
	return c;
	}
int main()
{

    #ifdef INPUT
       freopen("input.cpp", "r", stdin);
       freopen("output.cpp", "w",stdout);
   	#endif
   	int t;
   	cin>>t;
   	for(i,0,t)
   	{
   		string s;
   		int k;
   		cin>>s>>k;
   		int w=flip(s,k);
   		if(w==-1)
   		cout<<"Case #"<<(i+1)<<": "<<"IMPOSSIBLE"<<endl;
   		else
   		cout<<"Case #"<<(i+1)<<": "<<w<<endl;
	   }
	   return 0;
}
	   
