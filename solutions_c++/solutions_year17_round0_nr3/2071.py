#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>
#include <map>
using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 120


int main()
{
	freopen("c.in","r",stdin);
	//freopen("c.out","w",stdout);
	
	

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		ll n,k,filled=0;
		map<ll,ll> empty_slots;
		cin>>n>>k;
		
		empty_slots[n]=1;
		while(filled<k){
			//cout<<"MAP:\n";
			//for(map<ll,ll>::iterator it=empty_slots.begin();it!=empty_slots.end();it++){
			//	cout<<it->F<<' '<<it->S<<endl;
			//}
			//cout<<"______\n";
			ll empty_now_size =prev(empty_slots.end())->F;
			ll empty_now_count=prev(empty_slots.end())->S;
			ll right_insert=(empty_now_size>>1);
			ll left_insert =(empty_now_size-1)>>1;
			
			if(empty_now_count+filled>=k){
				cout<<right_insert<<' '<<left_insert;
				break;
			}
			//cout<<empty_now_size<<' '<<empty_now_count<<"    "<<right_insert<<' '<<left_insert<<endl;

			empty_slots.erase(prev(empty_slots.end()));

			if(empty_slots.find(right_insert)!=empty_slots.end())
				empty_slots[right_insert]+=empty_now_count;
			else
				empty_slots[right_insert]=empty_now_count;

			if(empty_slots.find(left_insert)!=empty_slots.end())
				empty_slots[left_insert]+=empty_now_count;
			else
				empty_slots[left_insert]=empty_now_count;

			filled+=empty_now_count;
		}

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}