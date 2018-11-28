#include<bits/stdc++.h>
#define mpr make_pair
#define ff first
#define ss second
#define pb push_back
#define ll long long 
#define MAXLEN 500
using namespace std;

typedef priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >, std::greater<pair<int,pair<int,int> > > > PQ;

//scanf ("%[^\n]%*c",inp);

unsigned long long  dp[MAXLEN][10];
unsigned long long tidy[MAXLEN];

void precompute(){
	
	for(int i=1;i<10;i++){
		dp[1][i]=1;
	}
	
	
	for(int len=2;len<=MAXLEN;len++){
		
		for(int i=1;i<10;i++){
			
			for(int j=9;j>=i;j--){
				
				dp[len][i]+=dp[len-1][j];
			}
			
		}		
	}
	
	for(int i=1;i<=MAXLEN;i++){
		
		for(int dig=1;dig<10;dig++)
			tidy[i]+=dp[i][dig];
	}
	
	
}

bool isTidy(long long int N){
	
	int prev=N%10;
	N/=10;
	while(N>0){
		
		int curr;
		curr=N%10;
		if(curr>prev)
			return false;
		prev=curr;
		N/=10;
						
	}
	
	return true;
	
}
long long int getNum(string str){
	
	long long ans=0;
	for(int i=0;i<str.size();i++){
		ans=ans*10+(str[i]-'0');
	}
	
	return ans;
}

long long int brute(string str){
	
	long long int N=getNum(str);

	for(long long int i=N;i>=0;i--){
		if(isTidy(i)){
		
			return i;
		}
		
	}
	
}

string getLastTidy(string str){
	
	for(int i=0;i<str.size()-1;i++){
		if(str[i]<=str[i+1])
			continue;
		else{
			
			if(str[i]=='1'){
				return getLastTidy(string(str.size()-1,'9'));
			
			}
			
			string prefix=string(str.begin(),str.begin()+i);
			prefix.push_back(str[i]-1);
			return getLastTidy(prefix+string(str.size()-(i+1),'9'));
						
		}
			
		
	}
	
	return str;
	
}

int main(){
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	
	
	int te,t=1;
	scanf("%d\n",&te);
	
	while(t<=te){
		
	
	string str;
	cin>>str;
		
	cout<<"Case #"<<t<<": "<<getLastTidy(str)<<endl;
	
	t++;
	}

return 0;	
}

