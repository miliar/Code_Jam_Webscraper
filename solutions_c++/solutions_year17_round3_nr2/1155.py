#include<bits/stdc++.h>

using namespace std;

int t,n,m;

struct intr
{
	int start;
	int end;
	int type;
	//1 - A interval
	//2 - B interval
	//3 - diff
};

struct intr2 
{
	int dur;
	int type;
};

bool cmp ( const intr &a1, const intr &a2)
{
	return a1.start<a2.start;
}
bool cmp2 ( const intr2 &a1, const intr2 &a2)
{
	return a1.dur<a2.dur;
}

intr a[1024];
intr2 b[1024]; // inverse

int sum_of_diff,sum_a,sum_b;
int diff_splits;
int cnt;

void input()
{
	sum_of_diff=0; diff_splits=0;
	sum_a=0;
	sum_b=0;
	cnt=0;
	cin>>n>>m;
	for(int i=0;i<n;i++)
	{
		cin>>a[i].start>>a[i].end;
		sum_a += a[i].end-a[i].start;
		a[i].type=1;
	}
	for(int i=0;i<m;i++)
	{
		cin>>a[n+i].start>>a[n+i].end;
		sum_b += a[n+i].end-a[n+i].start;
		a[i].type=2;
	}
	sort(a,a+(n+m),cmp);
	a[n+m].start=a[0].start+1440;
	a[n+m].end=a[0].end+1440;
	a[n+m].type=a[0].type;
	cnt = 0;
	//cout<<a[0].start<<"-"<<a[0].end<<" ("<<a[0].type<<")"<<endl;
	for(int i=1;i<=n+m;i++)
	{
		//cout<<a[i].start<<"-"<<a[i].end<<" ("<<a[i].type<<")"<<endl;
		if(a[i-1].type==a[i].type) {
			b[cnt].type = a[i-1].type;
			b[cnt].dur = a[i].start-a[i-1].end;
			cnt++;
		}
		else
		{
			sum_of_diff+=a[i].start-a[i-1].end;
			diff_splits++;
		}
	}
	sort(b,b+cnt,cmp2);
}

int solve()
{
	//cout<<" sumA = "<<sum_a<<" sumB = "<<sum_b<<endl;
	//cout<<" there are "<<sum_of_diff << " units that can be split, min splits =  " << diff_splits << endl;
	//cout<<" there are "<<cnt<<" intervals between 2 same " <<endl;
	for(int i=cnt-1;i>=0;i--)
	{
		if(b[i].type==1)
			sum_a+=b[i].dur;
		else sum_b+=b[i].dur;
		
		int d = sum_a-sum_b;
		if(d<0) d=-d;
		if(d>sum_of_diff)
		{
			sum_of_diff+=b[i].dur;
			if(b[i].type==1) sum_a-=b[i].dur;
			else sum_b-=b[i].dur;
			diff_splits+=2;
		}
	}
	
	return diff_splits;
}

int main()
{
	cin.sync_with_stdio(0);
	cin.tie(0);
	cin>>t;
	for(int cas=1;cas<=t;cas++)
	{
		input();
		cout<<"Case #"<<cas<<": "<<solve()<<'\n';
	}
	return 0;
}
