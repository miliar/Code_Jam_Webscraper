#include <iostream>
#include <string>
#include <iterator>
#include <algorithm>

using namespace std;
/*
bool tidy(long long int num)
{
    int last    =   9;
    while(num)
    {
        if( (num%10)    <=  last    )
        {
            last    =   num%10;
            num/=10;
        }
        else
        {
            return false;
        }
    }
    return true;
}
*/

bool samedigit(long long int nm){
    int last    =   nm%10;
    while(nm){

        if(last !=  nm%10)
            return  false;
        nm/=10;
    }
    return true;
}

long long int maketidy(long long int num){

    if(num  <=  9){
        return num;
    }

    if(samedigit(num)){
        return num;
    }

    //make a tidy number
    long long int tidy_num  =   0;
    long long int mul   =   1;
    int last,last_1;

    while(num){
        last    =   num%10;
        if(num >=   10) last_1  =   (num/10)%10;
        else{
            tidy_num    +=  (last*mul);
            num/=10;
            mul*=10;
            break;
        }
        if(last !=  0   &&  last_1  !=0 ){
            if(last <   last_1){
                tidy_num    =   (mul*10)-1;
                num/=10;
                mul*=10;
                num--;
                /*
                last    =   9;
                tidy_num    +=  (last*mul);
                num/=10;
                num--;
                mul*=10;
                */
            }
            else{
                tidy_num    +=  (last*mul);
                num/=10;
                mul*=10;
            }
        }
        else if(last ==  0   &&  last_1  !=  0){
            last    =   9;
            tidy_num    +=  (last*mul);
            num/=10;
            num--;
            mul*=10;
        }
        else if(last    !=  0   &&  last_1  ==  0){
            last    =   9;
            tidy_num    +=  (last*mul);
            num/=10;
            mul*=10;
        }
        else if(last    ==  0   &&  last_1  ==  0){
            last    =   9;
            tidy_num    +=  (last*mul);
            num/=10;
            mul*=10;
        }
    }

    return  tidy_num;
}

int main()
{
    int t,Case =    1;
    long long int n;
    cin >>  t;

    while(t--)
    {

        cin >>  n;
        cout    <<  "Case #"  << Case++ << ": " <<  maketidy(n) <<  '\n';
        /*
        for(;   n   >   0   ;n--)
        {
            if(tidy(n))
            {
                cout    <<  n   <<  '\n';
                break;
            }
        }
        */
    }

    return 0;
}
