#include <bits/stdc++.h>
using namespace std;
#define f(i,n)	for(int i=0;i<n;i++)

class pony
{
public:
	int in,val;
	pony(int a,int b)
	{
		in=a,val=b;
	}
};

bool compare(pony a,pony b)
{
	return a.val>b.val;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	f(ii,t)
	{
		int n;
		cin>>n;
		char h[6]={'R','O','Y','G','B','V'};
		char s[3]={'R','Y','B'};
		bool flag=0;
		vector<pony> vec;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;
		string out="";

		vec.push_back(pony(0,r));
//		vec.push_back(pony(1,o));
		vec.push_back(pony(1,y));
//		vec.push_back(pony(3,g));
		vec.push_back(pony(2,b));
//		vec.push_back(pony(5,v));

		sort(vec.begin(),vec.end(),compare);
//		cerr<<vec[0].in<<vec[1].in<<vec[2].in<<"\n";
		if(vec[0].val>vec[1].val+vec[2].val)
		{
			flag=1;
			printf("Case #%d: IMPOSSIBLE\n",ii+1);
			continue;
		}
		int in=1;
		while(vec[1].val>0 || vec[2].val>0)
		{
			if(vec[in].val==0){
				if(in==1)	in=2;
				else	in=1;
			}
			out+=s[vec[in].in];
			vec[in].val--;
			if(in==1)	in=2;
			else	in=1;
		}
		in=0;
		int l=out.size(),fp=0;
		while(in<l-1)
		{
			if(out[in]==out[in+1])	break;
			in++;
		}
		if(in==l-1 && out[l-1]==out[0])	fp=0;
		if(in<l)
		{
			fp=in+1;
		}
//		cerr<<"Before "<<out<<"\n";
		char tofill=s[vec[0].in];
//		cerr<<ii+1<<tofill<<"\n";
		int val=vec[0].val;
		while(val>0)
		{
			out.insert(out.begin()+fp,tofill);
			val--;
			fp+=2;
			fp%=out.size();
		}
		for(unsigned int i=1;i<out.size()-1;i++)
		{
			if(out[i]==out[i-1] || out[i]==out[i+1])
			{
				flag=1;
				break;
			}
		}
		if(flag)
		{
//			cerr<<out<<"\n";
			printf("Case #%d: IMPOSSIBLE\n",ii+1);
			continue;
		}

		printf("Case #%d: %s\n",ii+1,out.c_str());

	}

	return 0;
}
