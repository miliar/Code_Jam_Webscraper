#include <deque>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <ctime>
#include <cstdio>
#include <math.h>
using namespace std;

#define pb push_back


bool check(long  long int N){
    int last;
    while(N!=0){
        last = N%10;
        N/=10;
        if(last<N%10)
            return false;
    }
    return true;
}


long long int findNextTidy(long long int N){

    //modify once and check, at most will do modification 19 times.
    //1-find inflectino point, 2 set the rest to 9s and decrement current by 1,
    //check(N)  if false do the process on new N. Until correct N is found.
    //

    while(!check(N)){
        //find inflection point// checkout all digits into array; then compre them to find inflection point.
        //
        std::deque<int> digits;
        long long int M=N;
        int len=0;
        do {
            digits.push_front( M % 10);
            M /= 10;
            len++;
        } while (M>0);
        // find inflection point if any
        for(int i=0; i<len-1;i++){
                //turn all the numbers after that to 9s and decrement htis number;
            if(digits[i]>digits[i+1]){
                digits[i]--;
                while(i<len){
                        i++;
                    digits[i]=9;
                }
                break;
            }
        }
        N = 0;
        for(int i=0;i<len; i++){
            //printf("%d,",digits[i]); convert back to a number
            N+= (long long int ) ceil(pow(10,len-i-1))*digits[i];
        }

    }

    return N;
}


int main() {

    freopen("outputLarge.txt","w",stdout);

    long long int N;
    int T;

    cin>>T;

    for(int i=0; i<T; i++){
        scanf("%lld",&N);
        printf("Case #%d: ",i+1);
        if(check(N))
            cout<<N<<endl;
        else
            cout<<findNextTidy(N)<<endl;
    }
    return 0;
}

