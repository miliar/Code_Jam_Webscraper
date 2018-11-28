#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int x=1;x<t+1;x++){
        string seq;
        int flips,counter=0;
        bool notCool=false;
        cin>>seq>>flips;
        seq[0]=='0';
        //Head check
        if(seq[0]=='-'){
            for (int i=0;i<flips;i++){
                if(seq[i]=='+')seq[i]='-';
                else seq[i]='+';
            }
            counter++;
        }
        //Tail checker
        if(seq[seq.length()-1]=='-'){
            for (int i=0;i<flips;i++){
                if(seq[seq.length()-1-i]=='+')seq[seq.length()-1-i]='-';
                else seq[seq.length()-1-i]='+';
            }
            counter++;
        }

        //main checker
        for (int i=0;i<seq.length()-flips+1;i++){
            //cout<<i<<" "<<seq<<"  ";
            if (seq[i]=='-'){
                for (int j=0;j<flips;j++){
                    if(seq[i+j]=='+')seq[i+j]='-';
                    else seq[i+j]='+';
                }
                //cout<<i<<" "<<seq<<"  ";
                counter++;
            }
        }
        //last checker
        for (int i=seq.length()-flips;i<seq.length();i++){
            if (seq[i]=='-')notCool=true;
        }

        if (notCool==true)cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<x<<": "<<counter<<endl;
    }
    return 0;
}
