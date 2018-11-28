#include<bits/stdc++.h>
#define lli long long int
#define pi pair<int,int>
#define plli pair<lli,lli>
#define m_p make_pair
#define vi vector<int>
#define vlli vector<lli>
#define vc vector<char>
#define si set<int>
#define slli set<lli>
#define stklli stack<lli>	//push - pop
#define qulli queue<lli>	//push - pop
#define listlli	list<lli>	//push_back/front() pop_back/front()
#define p_qdec priority_queue< lli , vector < lli > > //for decreasing 5,3,2
struct compare{

	bool operator()(const lli& l,const lli& r){

		return l>r;

	}

};
#define p_qinc priority_queue< lli , vector < lli > ,compare>	//increasing order 0,1,2,3

#define ff(i,a,b) for(i=a;i<b;i++)
#define fb(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define c(a) cin>>a
#define o(a) cout<<a<<endl
#define sf(a) scanf("%d",&a)
#define pf(a) printf("%d\n",a)
using namespace std;
/*
int *ptr;
ptr = (int*) malloc(num * sizeof(int));
memset(arr,0, sizeof(arr)); //only for zero value
free(ptr);
*/
/*
int Is_Tidy_No(long long int n){
	int temp=n%10;
	n=n/10;
	while(n!=0){

		if(n%10<=temp){
			temp=n%10;

		}else{
			return 0;
		}
		n=n/10;
	}
	return 1;
}
*/
long long int Find_Tidy_No(long long int n){

	vector<int>v;
	while(n!=0){
		v.push_back(n%10);
		n=n/10;
	}
	int i=0;
	long long int ans=0;
	ff(i,0,v.size()-1){
		if(v[i]<v[i+1]){
			v[i]=9;
			v[i+1]--;
			for(int j=i-1;j>=0;j--){
				v[j]=9;
			}
	}
}
	for(i=v.size()-1;i>=0;i--) ans=ans*10+v[i];
	return ans;
}
int main(int argc, char const *argv[])
{
	int t,j=1;
	long long int n,ans;
	/*for(int i=0;i<1000000;i++){
		cout<<i<<endl;
	}*/
	sf(t);
	while(t-->0){
		cin>>n;
		ans=Find_Tidy_No(n);
		cout<<"Case #"<<j<<": "<<ans<<endl;
		j++;
	}
	return 0;
}
