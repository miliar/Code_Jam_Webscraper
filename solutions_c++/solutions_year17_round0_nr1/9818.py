#include<iostream>
#include<vector>
#include<list>
#include<sstream>
using namespace std;

stringstream sout;

void flipLeft(list<char> &s,const int &k){
    list<char>::iterator li = s.begin();
    for(int i=0;i<k;i++){
        *li=='+'?*li='-':*li='+';
        li++;
    }
}

void flipRight(list<char> &s,const int &k){
    list<char>::iterator li = s.end();
    for(int i=0;i<k;i++){
        *li=='+'?*li='-':*li='+';
        li--;
    }
}

int getNegCountLeft(list<char>& s, const int &k){
    int count = 0;
    list<char>::iterator li = s.begin();
    for(int i=0;i<k;i++){
        if(*li=='-')
            count++;
        else
            return count;
        li++;
    }
    return count;
}

int getNegCountRight(list<char>& s, const int &k){
    int count = 0;
    list<char>::iterator li = s.end();
    for(int i=0;i<k;i++){
        if(*li=='-')
            count++;
        else
            return count;
        li--;
    }
    return count;
}

void removeCornerHappy(list<char> &s){
    while(s.size() && s.front()=='+')    // while the first character is happy
        s.pop_front();
    while(s.size() && s.back()=='+')    // while the first character is happy
        s.pop_back();
}

void printFlips(list<char> s,const int &k,const int &t){
    int flips = 0;
    int negCount=0;
    removeCornerHappy(s);
    if(!s.size()){   // if s is empty (means that it was already all happy
        sout<<"Case #"<<t<<": "<<flips;
    }/*
    else if(s.size()<=k){
        negCount = getNegCountLeft(s,s.size());
        if(negCount==k)
            sout<<"Case #"<<t<<": "<<++flips;
        else if(negCount==0)
            sout<<"Case #"<<t<<": "<<flips;
        else
            sout<<"Case #"<<t<<": "<<"IMPOSSIBLE";
    }*/
    else{
        while(s.size()>=k){
            int l = getNegCountLeft(s,k);
            int r = getNegCountRight(s,k);
            if(l>=r)
                flipLeft(s,k);
            else
                flipRight(s,k);
            flips++;
            removeCornerHappy(s);
        }
        negCount = getNegCountLeft(s,s.size());
        /*if(negCount==k)
            sout<<"Case #"<<t<<": "<<++flips;
        else*/
        if(negCount==0)
            sout<<"Case #"<<t<<": "<<flips;
        else
            sout<<"Case #"<<t<<": "<<"IMPOSSIBLE";
    }
}

int main(){
    int T;
    cin>>T;
    for(int i=0;i<T;i++){
        string s;
        list<char> sl;
        int k;
        cin>>s;
        cin>>k;
        for(int i=0;i<s.size();i++)
            sl.push_back(s[i]);
        printFlips(sl,k,i+1);
        sout<<"\n";
    }
    cout<<sout.str();
    return 0;
}
