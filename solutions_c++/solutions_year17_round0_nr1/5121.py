#include <iostream>
#include <fstream>
#include <string>

using namespace std;
int a[1005];


int main(){
ifstream myfile("sample.txt");
ofstream ifile("large_output.txt");
int t;
myfile >> t;
for(int tt=1;tt<=t;tt++){
    string s;
    int k,ans=0;
    myfile >>s >> k;
    for(int i=0;i<s.length();i++){if(s.at(i)=='+') a[i]=1 ; else a[i] = 0; }
    //for(int j=0;j<s.length();j++) ifile<<a[j];
    //ifile<<endl;

    for(int i=0;i<s.length();i++){
        if(a[i]==0&&i+k-1<s.length()){
            for(int j=i;j<=i+k-1;j++)
            {a[j]=1-a[j];}
            ans++;
        }
        if(a[i]==0&&i+k-1>=s.length()){
            //ifile << i <<endl;
            ans=-1;break;

        }
        //for(int j=0;j<s.length();j++) ifile<<a[j];
        //ifile<<" "<<i<<endl;
    }
if(ans==-1)ifile << "Case #" << tt << ": "<<"IMPOSSIBLE" <<endl;
else
ifile << "Case #" << tt << ": "<<ans << endl;

}




return 0;
}
