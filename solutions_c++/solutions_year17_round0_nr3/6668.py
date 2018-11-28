#include<bits/stdc++.h>
#define ull unsigned long long
using namespace std;
struct comp1{

bool operator()(const pair<ull,pair<ull,ull> >& lhs,const pair<ull,pair<ull,ull> >& rhs )
{if(lhs.first==rhs.first)
return(lhs.second.first<rhs.second.first);
else return(lhs.first>rhs.first);
}             };


int main()
{   freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
	
	int t,case_val=1;
	cin>>t;
	while(t--)
	 {
	 	ull n,k;cin>>n>>k;
	 	set<pair<ull,pair<ull,ull> > ,comp1> heap;
		  set<pair<ull,pair<ull,ull> > >::iterator it,it1;
					pair<ull,pair<ull,ull> > p=make_pair(n,make_pair(1,n));
					heap.insert(p); it1=heap.begin();
					ull i=1;
						   //cout<<"Now"<<it1->first;
					while(i<=k)
					{
						it=heap.begin(); ull len=it->first;    //cout<<len<<endl;
						ull st=it->second.first,en=it->second.second; heap.erase(it);
						ull st1=st,end1=((st+en)/2);end1--;ull st2=end1+2,end2=en;  // cout<<end1<<" ";
						ull len1=end1-st1+1,len2=end2-st2+1;
						pair<ull,pair<ull,ull> > p1= make_pair(len1,make_pair(st1,end1));
						pair<ull,pair<ull,ull> > p2 =make_pair(len2,make_pair(st2,end2));
						 heap.insert(p1);
						 heap.insert(p2);
					if(i==k)
					{   if(len1>len2)
					{cout<<"Case #"<<case_val<<": "<<len1<<" "<<len2<<endl;
					}
					else{cout<<"Case #"<<case_val<<": "<<len2<<" "<<len1<<endl;
					}}
						
				i++;	}
	 	
	 	case_val++;}




return 0;
}
