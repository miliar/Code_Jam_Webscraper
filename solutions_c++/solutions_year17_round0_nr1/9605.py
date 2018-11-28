#include<iostream>
#include<fstream>
using namespace std;
void solve(string,int,int);
int counter = 0;
int main(){
    ofstream myfile;
    myfile.open("output.txt");
int n;
cin>>n;
string st;
int a;
for(int i=0;i<n;i++){
    cin>>st;
    cin>>a;
    solve(st,a,0);
    if(counter == -1) myfile<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    else myfile<<"Case #"<<i+1<<": "<<counter<<endl;
    counter = 0;
}
myfile.close();
return 0;
}
void solve(string a,int siz,int pos){
    if(pos == a.length()){
        return;
    }
    else{
        if(a[pos] == '+'){
            solve(a,siz,pos+1);
        }else{
            if(a.length()-pos < siz){
                    counter = -1;
                return;
            }else{
            counter++;
            int temp = pos;
            for(int i=0;i<siz;i++){
                if(a[pos] == '+') a[pos] = '-';
                else a[pos] = '+';
                pos++;
            }
            pos = temp;
            solve(a,siz,pos);
            }
        }
    }
}
