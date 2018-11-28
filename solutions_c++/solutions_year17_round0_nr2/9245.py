#include<bits/stdc++.h>
using namespace std;

string f(string s){

    int n = s.size();

    if(n==1) return s;

    string k = "";

    bool f = false;

    bool pp = false;

    int pos = 0;


    for(int i=0;i<n;i++){

        if(s[i+1]=='0') {
            //cout<<"here\n";
            f = true;
            pos = i;
            break;
        }
    }

    for(int i=0;i<n-1 && f==false;i++){

        if(s[i]>s[i+1]){

            pos = i;

            int j = 0;

            while(1){

                if(pos>0){

                    j = (int) (s[pos] - '0' + 0);

                    j--;

                    int r = (int) (s[pos-1] - '0' + 0);

                    if(r>j){
                        pos--;
                    }
                    else break;
                }
                else break;

            }

            if(pos==0){
                j = (int) (s[pos] - '0' + 0);

                j--;
            }

            k = "";


            for(int kk = 0;kk<pos;kk++){
                k += s[kk];
            }

            k += (j+'0');

            pp = true;

            for(int j = pos+1;j<n;j++){
                k += '9';
            }

            break;

        }
        else{

            k += s[i];

        }

    }

    if(pp==false){
        k += s[n-1];
    }



    if(f==true){

        k = "";

        while(s[pos]=='1' && pos!=-1){
            pos--;
        }

        if(pos==-1){
            for(int i=0;i<n-1;i++){
                k += '9';
            }
        }
        else{

            int j=0;

            while(1){

                if(pos>0){

                    j = (int) (s[pos] - '0' + 0);

                    j--;

                    int r = (int) (s[pos-1] - '0' + 0);

                    if(r>j){
                        pos--;
                    }
                    else break;
                }
                else break;

            }

            if(pos==0){
                j = (int) (s[pos] - '0' + 0);

                j--;
            }

            for(int i=0;i<pos;i++){
                k += s[i];
            }

            k += (j+'0');

            for(int i=pos+1;i<n;i++){
                k += '9';
            }

        }

    }

    return k;

}


int main(){

    int t;

    freopen("B-small-attempt4.in","rt",stdin);
    freopen("output.txt","wt",stdout);

    cin>>t;

    getchar();

    string s;

    for(int i=1;i<=t;i++){
        cin>>s;

        printf("Case #%d: ",i);

        cout<<f(s)<<"\n";

    }

}
