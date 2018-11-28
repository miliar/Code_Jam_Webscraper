#include<iostream>
#include<string>

using namespace std;


int main(){

    int T;
    long long N;
    cin>>T;

    for (int i=0;i<T;i++){

        cin>>N;

        if(N<10){
            cout<<"Case #"<<i+1<<": "<<N <<endl;
        }
        else{
            string s =std::to_string(N);
            int k=0;
            while (k<=s.size()-2){
                if(s[k] > s[k+1]){
                    int numberK = s[k] - '0'-1;
                    string subs =std::to_string(numberK);
                    s[k] = subs[0];
                    for(auto k1 = k+1;k1<s.size();k1++){
                        s[k1] = '9';
                    }
                    k=0;
                }
                else
                    k++;
            }
            long long tidy= stoll(s);
            cout<<"Case #"<<i+1<<": "<<tidy <<endl;
        }
    }
    return 0;
}
