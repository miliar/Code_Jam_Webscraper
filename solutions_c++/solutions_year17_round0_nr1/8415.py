#include<bits/stdc++.h>
using namespace std;

void coutMe(string a, int b=0){

    cout<<a<<" = "<<b<<endl;
}

void coutMe1(string a, string b=""){

    cout<<a<<" = "<<b<<endl;
}


int main(){

    FILE *in = freopen("A-large.in", "r", stdin);
    FILE *out = freopen("sample11.out", "w", stdout);

    int T;
    cin>>T;
    for(int i=1; i<=T; i++){

        string S ;
        cin>>S;
        int K ;
        cin>>K;
        stack<char> A;
        int c = 0;
        for(int j=0; j<S.length(); j++)
            A.push(S[j]);

        int flag = 1;
        string R = "";
        int N = 50;
    //    coutMe("A.size()", A.size());
        while(A.size() >= 1){

         //   coutMe("A.size()", A.size());

            if(A.top() == '+' && flag == 1){
                A.pop();
                if(A.size() == 0)
                    break;
            }

            if(A.top() == '-' || flag == 0){
                R += A.top();
                A.pop();
                if(A.size() == 0)
                    break;
                flag = 0;
            }

            if(R.length() == K){
           //     coutMe1("Flip,R",R);
                for(int j=R.length()-1; j>=0; j--){
                    if(R[j] == '+')
                        R[j] = '-';
                    else
                        R[j] = '+';
                    A.push(R[j]);
                }
                c += 1;
                R = "";
                flag = 1;
            }

           // coutMe1("R",R);
        }

        if(R.length() < K && R[0] == '-'){
            R ="-";
            flag = 3;
        }


        if(R.length() == K && R[0]=='-'){
            for(int j=R.length()-1; j>=0; j--){
                    if(R[j] == '+')
                        R[j] = '-';
                    else
                        R[j] = '+';
                }
            c += 1;
        }

        for(int j=0; j<R.length();j++)
        if(R[j] == '-'){
            flag = 3;
            break;
        }

        if(flag == 3)
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i<<": "<<c<<endl;

    }


    return 0;
}
