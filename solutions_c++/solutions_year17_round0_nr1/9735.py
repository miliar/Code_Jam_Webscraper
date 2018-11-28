#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main(){
    ifstream in("A-small.in");
    ofstream out("A-small.out");
    int i,j,k,t,n,flag,c,flipped;
    string s1,s2;
    in>>t;

    for(i=1; i<=t ;i++){
        in>>s1;
        in>>k;
        s2 = s1;
        c=0;
        flipped = 0;

        for(j=s2.length()-1;j>=k-1;j--){
            flag = 0;
            if(s2[j] == '-'){
                c++;
                for(n=j;n>j-k;n--){
                    if(s2[n] == '-')
                        s2[n] = '+';
                    else
                        s2[n] = '-';
                }
                if(s2 == s1){
                    flag = 1;
                    out<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
                    break;
                }
                //cout<<"string flipped "<<c<<"   "<<s2<<endl;
                j = s2.length()-1;
            }
            if(flipped == 0){
                flipped++;
                j = s2.length();
            }
            cout<<"case : "<<i<<" done"<<endl;
        }
        for(n=0;n<s2.length();n++){
            if(s2[n] == '-'){
                flag = 1;
                out<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
                break;
            }
        }
        if(flag != 1){
            out<<"Case #"<<i<<": "<<c<<endl;
        }
    }

    return 0;

}
