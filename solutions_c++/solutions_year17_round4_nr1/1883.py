#include<fstream>
#include<vector>
#include<iomanip>
#include<algorithm>
#include<math.h>
#include<set>
#include<stack>
#include<queue>
#include<string.h>
using namespace std;

ifstream cin ("A-small-attempt3.in");
ofstream cout ("ax.out");

int ca=0;

void doit(){
	
	int n,p;
	cin>>n>>p;
	ca++;
	
	int ans=0;
	int ate;
		
	if(p==2){
		int ass=0;
		int mid=0;
	
		for(int i=0;i<n;i++){
			cin>>ate;
			if(ate%2==0){
				mid++;
			}
			else{
				ass++;
			}
		}
		ans=mid;
		ans += (ass%2);
		ans += ass/2; 			
	}
	
	if(p==3){
		
		int mid=0;
		int ena=0;
		int dio=0;
		
		for(int i=0;i<n;i++){
			cin>>ate;
			if(ate%3==0){
				mid++;
			}
			if(ate%3==1){
				ena++;
			}
			if(ate%3==2){
				dio++;
			}
		}
		
		ans = mid;
		ans = ans + min(ena,dio);
		int y = min(ena,dio);
		ena -=y;
		dio -=y;
	
		if((dio!=0)||(ena!=0)){
			ans++;
			//mprostino emetrithike
		if(dio==0){
			//exoume mono assous
			ans += ena/3;
			if(ena%3==0){
				ans--;
			}
		}
		else{
			//exoume mono 2lia
						ans += dio/3;
			if(dio%3==0){
				ans--;
			}
			
		}
		}

		
	}
	
	if(p==4){
		
	}
	
	cout<<"Case #"<<ca<<": "<<ans<<endl;
	
}

int main(){
	
	int t;
	cin>>t;
	while(t--){
		doit();
	}
}
