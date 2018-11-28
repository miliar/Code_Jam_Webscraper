#include <bits/stdc++.h>
using namespace std;

int main() {
     //freopen("B-small-attempt0 (1).in","r",stdin);
    //freopen("murga3.out","w",stdout);
	long long it, t, n, r, o, v, g, b, y, i,cnt,k;
	cin>>t;
	for(it=0;it<t;it++)
	{
		cin>>n>>r>>o>>y>>g>>b>>v;
		if(r>n/2 || y>n/2 || b>n/2)
		{
			cout<<"Case #"<<it+1<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			pair<long long,char> col_ar[3];
			col_ar[0]=make_pair(r,'R');
			col_ar[1]=make_pair(y,'Y');
			col_ar[2]=make_pair(b,'B');
			sort(col_ar,col_ar+3);
			string s="";
			for(i=0;i<n;i++)
			{
				s+="0";
			}
			cnt=0;
			for(i=0;i<n;i+=2)
			{
				s[i]=col_ar[2].second;
				cnt++;
				if(cnt>=col_ar[2].first)
				{
					break;
				}
			}
			cnt=0;
			if(n%2==0)
			{
				k=n-1;
			}
			else
			{
				k=n-2;
			}
			for(i=k;i>=0;i-=2)
			{
				s[i]=col_ar[1].second;
				cnt++;
				if(cnt>=col_ar[1].first)
				{
					break;
				}
			}
			for(i=n-1;i>=0;i--)
			{
				if(s[i]=='0')
				s[i]=col_ar[0].second;
			}
			cout<<"Case #"<<it+1<<": "<<s<<endl;
		}
	}
	return 0;
}
