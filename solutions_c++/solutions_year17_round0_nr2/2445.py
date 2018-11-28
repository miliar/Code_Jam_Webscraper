/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: trungthanh
 *
 * Created on April 8, 2017, 5:18 PM
 */

#include <cstdlib>
#include <iostream>
#include <vector>
#include <bits/stl_vector.h>

using namespace std;

bool tidy(long int n, int& len, int& wrongpos,std::vector<int>& digits)
{
    
    std::vector<int> diff;
    long int backup = n;
    if (n < 10)
        return true;
    len = 1; 
    int last = n % 10;
    n= n/10;
    int curr = n%10;
    bool ok = true;
    //int wrongpos = 0;
    long int lastTidy = 0;
    int l; int c;
    digits.push_back(last);
    while (n > 0)
    {
        digits.push_back(curr);
        diff.push_back(last-curr);
        
        if (curr > last){
            ok = false;
            wrongpos = len;
            lastTidy = n;
            l = last;
            c = curr;
        }
            //return false;
        n = n / 10;
        last = curr;
        curr = n%10;
        len++;
    }
    
//    if (wrongpos > 0)
//    {
//        cout<<"last:"<<lastTidy<<" "<<c<<" "<<l<<endl;
//    }
    int p = wrongpos;
    wrongpos = len -wrongpos;

//    for (int i = 0; i < len; i++)
//        cout<<digits[len-i-1]<<" ";
//    cout<<endl<< "  ";
//    for (int i = 0; i < len-1; i++)
//        cout<<diff[len-2-i]<<" ";
//    cout<<endl;
    
    int k = p; 
    for (; k < len-1; k++)
        if (diff[k] > 0)
            break;
//    cout <<"vi tri thay doi  " << k <<endl;
    vector<int>& d2 = digits;
    d2[k]-=1;
    for ( int x = k-1; x>=0; x--)
        d2[x]=9;
//    for (int i = 0; i < len; i++)
//        cout<<d2[len-i-1]<<" ";
//    cout<<endl;
//    if (l > 0)
    return ok;
}
/*
 * 
 */
int main(int argc, char** argv) {
    
    int T;
  //  cout<< sizeof(long int)<<endl;
    cin >> T;
    
    for (int i = 0; i< T; i++)
    {
        long int num = 0;
        cin>> num;
        int len=0, wp = 0;
//        cout<<tidy(num, len, wp);
//        cout<<" "<<len << " "<<wp<<endl;
        std::vector<int> digits;
        if (tidy(num, len, wp, digits) )
            cout<<"Case #"<<i+1<<": "<<num<<endl;
        else{
            cout<<"Case #"<<i+1<<": ";
            for (int i = 0; i< len; i++)
                if (digits[len-i-1]> 0) cout<<digits[len-i-1];
            cout<<endl;
        }
    }

    return 0;
}

