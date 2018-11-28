#include<fstream>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<math.h>
#include<iomanip>
using namespace std;

ifstream cin ("A-large.in");
ofstream cout ("ax.out");

long long n,k;
int ca=1;

struct sort_pred {
    bool operator()(const std::pair<long double,long double> &left, const std::pair<long double, long double> &right) {
        return left.second > right.second;
    }
};

void doit(){

	cin>>n>>k;
	
	long double a,b;
	vector < pair < long double, long double > > pits;
	vector < pair < long double, long double > > pits2;
	//	giros , kikl
	for(int i=0;i<n;i++){
		cin>>a>>b;
		pits.push_back( make_pair( 2*M_PI*a*b , M_PI*a*a ) );
	}
	std::sort(pits.begin(), pits.end(), sort_pred());
	long double maxi=0;
	long double fi=0;
	for(int i=0;i<=n-k;i++){
		
	//	cout<<"we go for i = "<<i<<endl;
		fi=0;
		fi = pits[i].first + pits[i].second;
		
		pits2.clear();
		
		pits2.insert(pits2.begin(),pits.begin()+i+1,pits.end());
		
		std::sort(pits2.begin(), pits2.end());
		
		int kc =0;
		
		for(int j=pits2.size()-1;kc<k-1;j--){
			fi += pits2[j].first;
			kc++;
		}
		
	//	cout<<"second vector"<<endl;
		
	//	for(int j=0;j<pits2.size();j++){
	//		cout<<pits2[j].first<<" "<<pits2[j].second<<endl;
	//	}
		
	//	cout<<"fi produced is "<<fi<<endl;
		
		if(fi>maxi){
			maxi = fi;
		}
		
	}
	
	cout<<"Case #"<<ca<<": "<<setprecision(9)<<fixed<<maxi<<endl;
	ca++;
	
}

int main(){
	
	int t;
	cin>>t;
	while(t--){
		doit();
	}
	
}
