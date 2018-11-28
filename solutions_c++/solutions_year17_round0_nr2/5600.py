#include<fstream>
#include<vector>
using namespace std;

ifstream cin ("B-large.in");
ofstream cout ("ax.out");

int ca=0;

void doit(){
	string s;
	cin>>s;
	int a[s.size()];
	for(int i=0;i<s.size();i++){
		a[i] = (int)(s[i]) - (int)('0');
	}
	for(int k=0;k<100;k++){
		for(int i=0;i<s.size()-1;i++){
			if(a[i]>a[i+1]){
				a[i]--;
				for(int j=i+1;j<s.size();j++){
					a[j] = 9;
				}
				break;
			}
		}
	}
	cout<<"Case #"<<ca<<": ";
	for(int i=0;i<s.size();i++){
		if(a[i]!=0){
			for(int j=i;j<s.size();j++){
				cout<<a[j];
			}
			break;
		}
	}
	cout<<endl;
}

int main(){
	int n;
	cin>>n;
	while(n--){
		ca++;
		doit();
	}
}
