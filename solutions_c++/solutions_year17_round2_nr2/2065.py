#include <vector>
#include <sstream>
#include <iostream>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <cstdio>
#include <limits>
using namespace std;


void main2(){
	int N;//R 0, O 1, Y 2, G 3, B 4, V 5;
	cin>>N;
    int Z[6];
    string Z_str="ROYGBV";
    for(int i=0;i<6;i++) cin>>Z[i];
    for(int i=1;i<6;i+=2){
        if(Z[i]==Z[(i+3)%6] && Z[i]>0){
            if( Z[(i+1)%6]==0 &&Z[(i+2)%6]==0 &&Z[(i+4)%6]==0 &&Z[(i+5)%6]==0){
                while(Z[i]>>0){
                    cout<<Z_str[i]<<Z_str[(i+3)%6];
                    Z[i]--;
                }
                return;
            }else{
                cout<<"IMPOSSIBLE";
                return;
            }
        }
    }
    for(int i=1;i<6;i+=2){
        if(Z[i] > 0 && Z[i]>Z[(i+3)%6]-1){
            cout<<"IMPOSSIBLE";
            return;
        }
    }

    int ZZ[3];
    ZZ[0]=Z[0]-Z[3];
    ZZ[1]=Z[2]-Z[5];
    ZZ[2]=Z[4]-Z[1];
    
    int M=max(max(ZZ[0],ZZ[1]),ZZ[2]);
    int S=ZZ[0]+ZZ[1]+ZZ[2];
    if(S<2*M){
        cout<<"IMPOSSIBLE";
        return;
    }
    int I;
    for(int i=0;i<3;i++){
        if(ZZ[i]==M) I=i;
    }
    vector<string> output(S);
    int pos=0;
    for(int s=0;s<S;s++){
        if(Z[(2*I+3)%6]>0){
            stringstream ss;
            ss << Z_str[2*I] << Z_str[(2*I+3)%6] << Z_str[2*I];
            ss >> output[pos];
            Z[(2*I+3)%6]--;
        }else{
            output[pos]=Z_str[2*I];
        }
        ZZ[I]--;
        if(ZZ[I]==0) I=(I+1)%3;
        if(ZZ[I]==0) I=(I+1)%3;
        pos=pos+2;
        if(pos>=S){
            if(S%2==1){
                pos-=S;
            }else{
                pos=1;
            }
        }
    }

    for(int s=0;s<S;s++) cout << output[s];
}

int main3(){
    string s;
    cin>>s;
    int N=0;
    int Z[6];
    string Z_str="ROYGBV";
    for(int i=0;i<6;i++){
        Z[i]=0;
        for(auto c:s){
            if(c==Z_str[i]) Z[i]++;
        }
        N+=Z[i];
    }
    cout <<N;
    for(int i=0;i<6;i++) cout <<' '<<Z[i];
}

/*int main(){
    string core="B-small-attempt3";

    freopen ( (core+".out").c_str(), "r", stdin );
    freopen ( (core+".out_in").c_str(), "w", stdout );

	for(int t=0;t<99;t++){
        string s;
        cin >> s;
        cin >> s;

		main3();
		cout<<endl;
	}



}*/

int main(){
    //string core="test";
    string core="B-small-attempt4";
    freopen ( (core+".in").c_str(), "r", stdin );
    freopen ( (core+".out").c_str(), "w", stdout );
	int T;
	cin>>T;

	for(int t=0;t<T;t++){
		cout<<"Case #"<<t+1<<": ";
		main2();
		cout<<endl;
	}
    
    fclose (stdin);
    fclose (stdout);
}
