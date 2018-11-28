// Acroph created at 2017-04-08 15:23:17
// ptx9363@gmail.com for more cantact

#include <iostream>

using namespace std;
#define MAXLENGRH 20

int stringDiv2(char* number, char* numberdiv2){
    int temp[MAXLENGRH];
    for(int i=0;i<MAXLENGRH;i++) temp[i] = 0;
    
    int n = strlen(number);
    int carry = 0 ;
    for(int i=0;i<n;i++){
        temp[i] = (number[i] - '0' + carry * 10) / 2;
        carry = (number[i] - '0' + carry * 10) % 2;
    }
    
    int k = 0;
    if (temp[k] == 0)
        k++;

    int head = 0;
    for(;k<n;k++){
        numberdiv2[head] = temp[k] + '0'; 
        head++;
    }


    // zero 
    if (head > 0)
        numberdiv2[head] = 0;
    else{
        numberdiv2[0] = '0';
        numberdiv2[1] = 0;
    }
    return carry;
}


void stringCopy(char* src, char* dst){
    for(int i=0;i<MAXLENGRH;i++)
        dst[i] = src[i];
}

void stringAdd1(char* number, char* numberAdd1){
    int n = strlen(number);
    int temp[MAXLENGRH];
    for(int i=0;i<n;i++) temp[i] = number[n-1-i] - '0';

    temp[0] += 1;
    int carry = 0;
    for(int i=0;i<n;i++){
       int temp_ = (temp[i] + carry) % 10;
       carry = (temp[i] + carry) / 10;
       temp[i] = temp_;
    }
    
    if (carry > 0){
        n++;
        temp[n-1] = carry;
    }
    
    for(int i=0;i<n;i++){
        numberAdd1[i] = temp[n-1-i] + '0';
    }
    numberAdd1[n] = 0;
}

void stringMinus1(char* number, char* numberMinus1){
    int n = strlen(number);
    int temp[MAXLENGRH];
    for(int i=0;i<n;i++) temp[i] = number[n-1-i] - '0';

    temp[0] -=1;
    for(int i=0;i<n;i++){
        if (temp[i] < 0){
            temp[i+1] -= 1;
            temp[i] += 10;
        }
    }
    
    if (temp[n-1] == 0 && n-1>0)
        n--;
    for(int i=0;i<n;i++){
        numberMinus1[i] = temp[n-1-i] + '0';
    }
    numberMinus1[n] = 0;
}

bool isZero(char* number){
    if ((strlen(number) == 1 && number[0] == '0') || (strlen(number) == 0))
        return true;
    else
        return false;
}

int main(){
    int T;
    char number[MAXLENGRH];
    cin.getline(number, MAXLENGRH);
    T = atoi(number);

    char K[MAXLENGRH];
    for(int t=0; t<T; t++){
        cin.getline(number, MAXLENGRH, ' ');
        cin.getline(K, MAXLENGRH);

        char Kdiv2[MAXLENGRH], Kt[MAXLENGRH];
        stringCopy(K, Kt);
        int carry[MAXLENGRH] = {0};
        int head = 0;
        carry[head] = stringDiv2(Kt, Kdiv2);
        head++;

        
        while( ! isZero(Kdiv2)){
            stringCopy(Kdiv2, Kt);
            carry[head] = stringDiv2(Kt, Kdiv2);
            head++;
        }
        
        char numberAdd1[MAXLENGRH];
        stringAdd1(number, numberAdd1);

        char Ndiv2[MAXLENGRH], Nt[MAXLENGRH];
        stringAdd1(number, Nt);
        int carryN[MAXLENGRH] = {0};
        int headN = 0;
        carryN[headN] = stringDiv2(Nt, Ndiv2);
        headN++;

        while( ! isZero(Ndiv2)){
            stringCopy(Ndiv2, Nt);
            carryN[headN] = stringDiv2(Nt, Ndiv2);
            headN++;
        }
        

        char Nresult[MAXLENGRH];
        stringAdd1(number, Nt);
        stringCopy(Nt, Nresult);
        for(int i=0;i<head-1;i++){
            stringDiv2(Nt, Nresult);
            stringCopy(Nresult, Nt);
        }

        char Nminus[MAXLENGRH];
        stringMinus1(Nresult, Nminus);
        stringCopy(Nminus, Nresult);

        //compare
        bool need_add1 = false;
        for(int i=head-2; i >-1; i--){
            if (carryN[i] > carry[i]){
                need_add1 = true;
                break;
            }
            if (carryN[i] < carry[i]){
                need_add1 = false;
                break;
            }
        }

        if (need_add1){
            stringCopy(Nresult, Nt);
            stringAdd1(Nt, Nresult);
        }

        // calculate the left and right
        char Nleft[MAXLENGRH], Nright[MAXLENGRH];
        stringMinus1(Nresult, Nt);
        int cLeft = stringDiv2(Nt, Nleft);
        if (cLeft)
            stringAdd1(Nleft, Nright);
        else
            stringCopy(Nleft, Nright);

        cout << "Case #" << t+1 <<": " << Nright << " " << Nleft << endl;
    }
}
