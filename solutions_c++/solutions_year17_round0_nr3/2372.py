#include <iostream>

using namespace std;

int main(){
    unsigned int tc_count;
    cin >> tc_count;
    for (unsigned int tc=0;tc<tc_count;tc++){
        unsigned long long int toilet_c,human_c;
        cin >> toilet_c >> human_c;
        unsigned long int power;
        unsigned long long int base=1;
        for (power=0;true;power++){
            if (human_c>base){
                human_c-=base;
                base=base*2;
                continue;
            }
            else {
                break;
            }
        }
        unsigned long long int final_n;
        if (power==0){final_n=toilet_c;}
        else {
            unsigned long long int space_c=1;
            while(toilet_c%2==1&&power>0){
                power--;
                toilet_c--;
                toilet_c=toilet_c/2;
                space_c=space_c*2;
            }
            if (power==0){final_n=toilet_c;}
            else{
                unsigned long long int less_n,less_c,more_n,more_c;
                toilet_c=toilet_c/2;
                less_n=toilet_c-1;
                more_n=toilet_c;
                less_c=space_c;
                more_c=space_c;
                power--;
                for (unsigned long int i=0;i<power;i++){
                    unsigned long long int less_c_t,more_c_t;
                    less_c_t=0;
                    more_c_t=0;
                    if (less_n%2==1){
                        less_n--;
                        less_n=less_n/2;
                        less_c_t+=less_c*2;
                        more_n=more_n/2;
                        less_c_t+=more_c;
                        less_c=less_c_t;
                    }
                    else {
                        less_n=less_n/2;
                        more_n=less_n;
                        less_n--;
                        more_c_t+=more_c*2;
                        more_c_t+=less_c;
                        more_c=more_c_t;
                    }
                }
                if (less_n==0){final_n=more_n;}
                else {
                    if (human_c>more_c){final_n=less_n;}
                    else {final_n=more_n;}
                }
            }
        }
        unsigned long long int a,b;
        if (final_n%2==1){
            final_n--;
            a=final_n/2;
            b=final_n/2;
        }
        else {
            final_n=final_n/2;
            a=final_n;
            b=final_n-1;
        }
        cout << "Case #" << tc+1 << ": " << a << " " << b << '\n';
    }
    return 0;
}
