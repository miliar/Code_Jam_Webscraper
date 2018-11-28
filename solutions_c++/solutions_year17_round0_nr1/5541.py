#include <iostream>

using namespace std;


void change(string& S, int K, int from){


    for(int i=from; i<from+K; i++){

        if(S[i] == '+') S[i] = '-';
        else S[i] = '+';
    }

}


string solve(string S, int K){


    int num_times = 0;

    int n = S.size();

    int current_idx = -1;


    while(current_idx < n-1){

        current_idx++;

        if(S[current_idx] == '+') continue;

        if(n-current_idx < K) return "IMPOSSIBLE";

        change(S, K, current_idx);
        num_times++;



    }


    return to_string(num_times);


}



int main(int argc, char *argv[])
{
    int T, K;
    string S;

    cin>>T;


    for(int c=1; c<=T; c++){


        cin>>S>>K;

        cout<<"Case #"<<c<<": "<<solve(S, K)<<endl;

    }
    return 0;
}
