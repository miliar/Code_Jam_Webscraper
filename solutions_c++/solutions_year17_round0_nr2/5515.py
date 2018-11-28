#include <iostream>

using namespace std;

typedef unsigned long long int lli;

string solve(string N){


    int len = N.size();

    string last_tidy = string(len ,N[len-1]);


    for(int i=0; i<len-1; i++){


        if((N[i]-'0') <= (N[i+1] - '0')){

            last_tidy[i] = N[i];
        } else {

            int current_digit = (N[i]-'0') -1;

            while((i-1>=0) && (current_digit < (N[i-1] - '0'))){
                i--;
            }

            last_tidy[i] = (current_digit) + '0';

            for(int j=i+1; j<len; j++){

                last_tidy[j] = '9';
            }
           break;


        }
    }

    if(last_tidy[0] == '0') last_tidy.erase(last_tidy.begin());
    if(last_tidy.size() == 0) last_tidy = "0";
    return last_tidy;


}

int main(int argc, char *argv[])
{
    int T;

    cin>>T;

    for(int c=1; c<=T; c++){

        lli N;
        cin>>N;
        cout<<"Case #"<<c<<": "<<solve(to_string(N))<<endl;
    }


    return 0;
}
