#include<iostream>
#include<stdio.h>
#include <cmath>
using namespace std;


long long gettidynum(long long x){
    int flag = true;
    long long original = x;
    //cout << "num: " << x << endl;
    int length = 0, rem2 = 0, rem1 = x%10;
    do{
        rem2 = x%10;
        x = x/10;
        rem1 = x%10;
        //cout << "x: " << x<< ", rem1: "<< rem1 << ", rem2: " << rem2 << endl;

        if (rem2 < rem1){
            //cout << "!non-decreasing\n";


            int t = 0;
            while(x%10 == rem1){
                t++;
                x=x/10;
            }
            x=x*10 + rem1  -1;
            //cout << "x = " << x << ", t = " << t<< endl;
            for (int i = 0; i<t + length; i++){
                x = x*10 + 9;
                //cout << "\tx = "<< x << endl;
            }
            flag = false;
            break;
        }else{
            //cout << "we are good\n";
        }

        length++;
    }while(x >= 10);
    //cout << "x= " << x<< ", length: " << length << endl;
    return (flag == true)?original:x;
}


int main (){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int testcase;
    scanf("%d ", &testcase);

    for (int i = 0; i< testcase; i++){

        long long num;
        scanf("%lld ", &num);
        //cout << "num: " << num << endl;
        while(num!=gettidynum(num)) num = gettidynum(num);

        printf("Case #%d: %lld", i+1, num);

        if (i!=testcase-1)printf("\n");
    }

    return 0;
}
