#include<iostream>
#include<queue>
#include<utility>

using namespace std;

class Comparegap
{
public:
    bool operator()(pair<long,long> n1,pair<long,long> n2) {
        long gap1,gap2;
        gap1=n1.second-n1.first;
        gap2=n2.second-n2.first;
		if(gap1==gap2)
			return n1.first>n2.first;
		return gap1<gap2;
    }
};

int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("Cout.in","w",stdout);
	long unsigned t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		long res1,res2,l,r,n,k;
		priority_queue<pair<long,long>,vector<pair<long,long> >,Comparegap> gaps;
		cin>>n>>k;
		gaps.push(make_pair(0,n+1));
		for(int j=0;j<k;j++)
		{
			pair<long,long> cur= gaps.top();
		
			gaps.pop();
			long s=(cur.second-cur.first)/2 + cur.first;
			gaps.push(make_pair(cur.first,s));
			gaps.push(make_pair(s,cur.second));
			l=s-cur.first-1;
			r=cur.second-s-1;	
			
		}
		if(l>r)
		{
			res1=l;
			res2=r;
		}
		else{
			res1=r;
			res2=l;
		}

		if(i==t)	
			cout<<"Case #"<<i<<": "<<res1<<" "<<res2;
		else
			cout<<"Case #"<<i<<": "<<res1<<" "<<res2<<endl;
			
	}
}
