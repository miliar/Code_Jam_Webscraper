#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

void doWork(int t, char *s, int n){
    int k = 0;
    for(int i = 0; i < strlen(s); i++){
        if(s[i] == '-'){
            if(i + n > strlen(s)){
                cout << "Case #"<< t << ": IMPOSSIBLE" << "\n";
                return;
            }
            k++;
            for(int j = i; j < i+n; j++){
                if(s[j] == '-'){
                    s[j] = '+';
                }else{
                    s[j] = '-';
                }
            }
        }
    }
    cout << "Case #"<< t << ": " << k << "\n";
}

int main(){
	int t,t2, n;
	char s[1005];
    //ifstream f("file.in");
	cin >> t;
    //f>>t;
	while(t > 0){
		cin >> s >> n;
        //f>>s>>n;
		doWork(++t2, s, n);
		t--;	
	}
}
