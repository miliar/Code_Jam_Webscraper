#include <iostream>

using namespace std;

unsigned long long bigger(unsigned long long a, unsigned long long b){
    if (a%2){
        a = (a-1)/2;
    } else {
        a = a/2;
    }
    return a;
}


unsigned long long smaller(unsigned long long a, unsigned long long b){
    if (b==0 && a%2){
        return 0;
    }
    if (b==0){
        return (a-2)/2;
    }
    if (b%2){
        b = (b-1) / 2;
    } else {
        b = (b-2) / 2;
    }
    return b;
}

unsigned long long bigger_num(unsigned long long a, unsigned long long b, unsigned long long a_num, unsigned long long b_num){
    unsigned long long res = 0;
    if  (a%2) {
        res += (a_num*2);
    } else {
        res += a_num;
    }

    if (b==0){
        res += 0;
    } else if(b%2){
        res += 0;
    } else {
        res += b_num;
    }
    return res;
}

unsigned long long smaller_num(unsigned long long a, unsigned long long b, unsigned long long a_num, unsigned long long b_num){
    unsigned long long res = 0;
    if  (a%2) {
        res += 0;
    } else {
        res += a_num;
    }

    if (b==0){
        res += 0;
    } else if(b%2){
        res += b_num*2;
    } else {
        res += b_num;
    }
    return res;
}


int main()
{
    int t;
    cin >> t;
    for(int c = 1; c <= t; c++){
        unsigned long long n, k;
        cin >> n >> k;
        unsigned long long big=n, small=0, LS, RS;
        unsigned long long big_num=1, small_num=0;

        while (true){
            //cout << big << '\t' << big_num<< '\t'<< k << endl;
            if (k <= big_num){
                LS = (big-1)/2;
                RS = big-1-LS;
                break;
            } else {
                k -= big_num;
            }
            //cout << small << '\t' << small_num <<'\t'<< k << endl;
            if (k <= small_num){
                LS = (small-1)/2;
                RS = small-1-LS;
                break;
            } else {
                k -= small_num;
            }

            unsigned long long b, s;
            b = bigger(big, small);
            s = smaller(big, small);
            unsigned long long b_num, s_num;
            b_num = bigger_num(big, small, big_num, small_num);
            s_num = smaller_num(big, small, big_num, small_num);
            big = b;
            small = s;
            big_num = b_num;
            small_num = s_num;
            //cout << big << '\t' << small << '\t' << big_num << '\t' << small_num << '\t'<< k<< endl;
        }


        cout << "Case #" << c << ": " << max(LS, RS) << ' ' << min(LS, RS) << endl;
    }
    return 0;
}
