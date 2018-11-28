#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n;
int fi;
vector<int> num;
bool check()
{
	num.clear();
	ll k=n;
	fi=9;
	bool flag=true;
	while(k)
	{
		if(k%10>fi) flag=false;
		fi=k%10;
		num.push_back(k%10);
		k/=10;
	}
	return flag;
}
void ioinit()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
}
int main()
{
	ioinit();
	int T,kase=1;
	cin>>T;
	while(T--)
	{
		cin>>n;
		printf("Case #%d: ",kase++);
		if(check()) cout << n << endl;
		else
		{
			reverse(num.begin(),num.end());
			for(int i=0;i+1<num.size();i++)
			{
				if(num[i]>num[i+1])
				{
					int k=i,pre=num[i];
					while(k>=0&&num[k]==pre) k--;
					++k;
					num[k]=pre-1;
					for(int j=k+1;j<num.size();j++)
						num[j]=9;
					break;
				}
			}
			int i=0;
			while(num[i]==0) i++;
			for(;i<num.size();i++)
				printf("%d",num[i]);
			puts("");
		}
	}
	return 0;
}
