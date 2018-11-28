#include <iostream>

using namespace std;

int check_length(int a)
{
    int length;
    for(length = 1; a > 0 ;length++)
    {
        a = a/10;
    }
    length--;
    return length;
}
int answer(int a)
{

   
    int len;
    len = check_length(a);
    
    if(len==18){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    int dig14 =(a/10000000000000) % 10;
    int dig15 =(a/100000000000000) % 10;
    int dig16 =(a/1000000000000000) % 10;
    int dig17 =(a/10000000000000000) % 10;
    int dig18 =(a/100000000000000000) % 10;
        if(dig18<=dig17&&dig17<=dig16&&dig16<=dig15&&dig15<=dig14&&dig14<=dig13&&dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    
      if(len==17){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    int dig14 =(a/10000000000000) % 10;
    int dig15 =(a/100000000000000) % 10;
    int dig16 =(a/1000000000000000) % 10;
    int dig17 =(a/10000000000000000) % 10;
        if(dig17<=dig16&&dig16<=dig15&&dig15<=dig14&&dig14<=dig13&&dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    
    if(len==16){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    int dig14 =(a/10000000000000) % 10;
    int dig15 =(a/100000000000000) % 10;
    int dig16 =(a/1000000000000000) % 10;
        if(dig16<=dig15&&dig15<=dig14&&dig14<=dig13&&dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==15){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    int dig14 =(a/10000000000000) % 10;
    int dig15 =(a/100000000000000) % 10;
    
        if(dig15<=dig14&&dig14<=dig13&&dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==14){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    int dig14 =(a/10000000000000) % 10;
    
        if(dig14<=dig13&&dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    
    if(len==13){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    int dig13 =(a/1000000000000) % 10;
    
        if(dig13<=dig12&&dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==12){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    int dig12 =(a/100000000000) % 10;
    
        if(dig12<=dig11&&dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
     if(len==11){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    int dig11 =(a/10000000000) % 10;
    
        if(dig11<=dig10&&dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==10){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    int dig10 =(a/1000000000) % 10;
    
        if(dig10<=dig9&&dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    
    if(len==9){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    int dig9 = (a/100000000) % 10;
    
        if(dig9<=dig8&&dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==8){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    int dig8 = (a/10000000) % 10;
    
        if(dig8<=dig7&&dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==7){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    int dig7 = (a/1000000) % 10;
    
        if(dig7<=dig6&&dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
        
    }
    if(len==6){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    int dig6 = (a/100000) % 10;
    
        if(dig6<=dig5&&dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
        
    }
    
    if(len==5){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    int dig5 = (a/10000) % 10;
    
        if(dig5<=dig4&&dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
        
    }
    if(len==4){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    int dig4 = (a/1000) % 10;
    
        if(dig4<=dig3&&dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
        
    }
    
    if(len==3){
    int dig1 = a % 10;
    int dig2 = (a/10) % 10;
    int dig3 = (a/100) % 10;
    
    
    if(dig3<=dig2&&dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==2)
    {
       int dig1 = a % 10;
       int dig2 = (a/10) % 10; 
       if(dig2<=dig1)
    {
        return a;
    }
    else 
    {
        a--;
        answer(a);
    }
    }
    if(len==1)
    {
        return a;
    }
}

int main()
{
    int N=0;
    int S[N];
    
   cin>>N;
   for(int i=0;i<N;i++)
   {
     cin>>S[i];   
   }
   for(int j=0;j<N;j++)
   {
       cout<<"Case #"<<j+1<<": "<<answer(S[j])<<endl;
   }
   //cout<<S[1];
   return 0;
}


