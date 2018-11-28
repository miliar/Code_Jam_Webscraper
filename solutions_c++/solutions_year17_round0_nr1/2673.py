#include <iostream>
#include <string>

using namespace std;
int main() {
	freopen ("output1.txt","w",stdout);
	freopen ("A-large.txt","r",stdin);
	int t;
	cin >> t;
	string s[100];
	int k[100];
	for (int i = 0;i<t;i++) {
		cin >> s[i];
		cin >> k[i];
	}
	for(int i=0;i<t;i++){
	    bool posible=true;
	    int answer=0;
	    for(int j=0;j<s[i].length();j++){
	            if(s[i][j]=='-'){
	                    if((s[i].length()-j)<k[i]){
	                            posible=false;
	                            break;
	                        }else{
	                                answer++;
	                                for(int r=j;r<j+k[i];r++){
	                                        if(s[i][r]=='-'){
	                                                s[i][r]='+';
	                                            }else{
	                                                s[i][r]='-';
	                                                }
	                                    }
	                            }
	                }
	        }
	        cout<<"Case #"<<i+1<<": ";
	        if(posible){
	            cout<<answer<<endl;
	            }else{
	                cout<<"IMPOSSIBLE"<<endl;
	                }
    }
	return 0;
}


