#include<iostream>
#include<fstream>

using namespace std;

int main(){
ifstream in("B-large.in");
ofstream out("outB.txt");
int T,j;
string s,token="";
in >> T;
for(int t = 1,j=0; t <= T; t++,j=0){
    in >> s;
    cout << t << " " << s << endl;
    int a[s.size()];
    for(int i=s.size()-1;i>=0;i--)a[i] = (int)(s.at(i))-'0';
    for(int i=1;i<s.size();i++){
    if(a[i] < a[i-1]){
        for(j=i-1;j>0;j--){
            if(a[j] > a[j-1])break;
        }
        a[j]--;
        for(j+=1;j<s.size();j++)a[j]=9;


    }
    }
    out <<"Case #" << t<<": ";
    for(int i = 0 ; i < s.size();i++)
    if(a[i]!=0)out << a[i];
    out << endl;

}
out.close(); in.close();
return 0;
}
