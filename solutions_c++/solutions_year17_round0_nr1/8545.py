#include <iostream>
#include <string.h>

using namespace std;


int T,K,len,flipNum;
bool result;
char input[1000];
char *message = "Case #";
char *no = "IMPOSSIBLE";
void flip(int k, int index, int D);
int getMin();
int main() {

    cin>>T;

    for(int t=0; t<T; t++) {

        cin>>input;
        cin>>K;
        len = strlen(input);

        getMin();
        cout<<message<<t+1<<": ";
        if(result) cout<<flipNum<<endl;
        else cout<<no<<endl;
    }
    return 0;
}


void flip(int K, int index, int D) {

    //left
    if(D==0) {
        for(int k=0; k<K; k++ ) {
            if(input[index+k] == '+') input[index+k]='-';
            else  input[index+k]='+';
        }
    }

    else {
       for(int k=0; k<K; k++ ) {
            if(input[index-k] == '+') input[index-k]='-';
            else  input[index-k]='+';
        }
    }
}
int getMin() {
    flipNum=0;
    result = true;
    int L,R;
    L=0;
    R=len-1;

    //cout<<input<<"L = "<<L<<" R = "<<R<<endl;

    while(L<R) {
        //check L
            //flip
            if(input[L] == '-' ) {
                flipNum++;
                flip(K,L,0);
               if(L+K-1 > R) result = false;
            }


            L++;

           // cout<<input<<"L = "<<L<<" R = "<<R<<" flip = " <<flipNum<<" result = "<<result<<endl;

        //check R

            //flip
            if(input[R]=='-' ) {
                flipNum++;
                flip(K,R,1);
              if(R-K+1 < L) result = false;
            }

            R--;

           //cout<<input<<"L = "<<L<<" R = "<<R<<" flip = " <<flipNum<<" result = "<<result<<endl;
    }

    if(input[L] == '-') result = false;

}










