#include <bits/stdc++.h>
using namespace std;

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("inp.txt","r",stdin);
		freopen("out1.txt","w",stdout);
	#endif
    long long int T,n,a[100],x,i,p,k,mod,b[100],l;
	cin >> T;
	for(x=1;x<=T;x++)
	{
		cin >> n;
		k=n;
        l=1;
        while(k!=0)
		{
			mod=k%10;
			a[l]=mod;
			k/=10;
			l++;
		}
		l--;
		k=l;
		p=1;
		for(p=1;p<=l;p++)
		{
			b[p]=a[k];
			k--;
		}
		while(1)
		{
			for(i=1;i<=l-1;i++)
			{
				if(b[i]>b[i+1])
				break;
			}
			if(i==l)
			break;
			b[i]--;
			i++;
			for(i=i;i<=l;i++)
			{
				b[i]=9;
			}
		}
		cout << "Case #" << x << ':' << ' ';
		if(b[1]!=0)
		cout << b[1];
		for(i=2;i<=l;i++)
		{
			cout << b[i];
		}
		cout << endl;
	}

    return 0;
}
