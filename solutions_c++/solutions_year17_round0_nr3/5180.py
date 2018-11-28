#include<iostream>
#include<cmath>
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

//long countLevel=0;
//long countLevelNumber= 1;
long k1,i1; 
vector<int>v;

struct node
{
    long data;
    long level;
   struct node* left;
  struct  node* right;
};




 
void insertNode(node *dot,long value,long level){
    
    if(dot->level == i1){
     v.push_back(dot->data);
   

    // countLevelNumber+=1;
    return;
      
}

        

    
    
    node* temp1 = new node;
    node* temp2 =  new node;
    dot->left = temp1;
    dot->right = temp2;

    int d=value;
    dot->left->level = level + 1;
    dot->right->level = level + 1;
    
    
    if(d%2!=0){
        (dot->right)->data =d/2;
        (dot->left)->data = d/2;
    }
    else{
        (dot->right)->data =d/2;
         if(d==1 ||d== 0)
           (dot->left)->data = 0;

         else  
        (dot->left)->data = d/2-1;   
    }
    
    insertNode(dot->right,dot->right->data,dot->right->level);
    insertNode(dot->left,dot->left->data,dot->right->level);
     
    
     
     
}
    
    
    
int main(){
    node* root =new node;
    int t;
    long n,k;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
    scanf("%ld%ld",&n,&k);

    long j1,m1=0;
    
    j1=0;i1=0;k1=k;
    
    while(k1>j1){
         m1=j1;
         j1=pow(2.0,i1)+j1;
         i1+=1;
        // cout<<m1<<" b"<<j1<<endl;
      }
     i1=i1-1;
     k1=k1-m1;
     if(k1==0)
      k1=pow(2.0,i1);
   //cout<<"level"<<i1<<endl<<"value"<<k1<<endl<<"m1"<<m1;
 
     
    root->data = n;
    root->level = 0;
    // countLevel=0;
     //countLevelNumber= 1;

    insertNode(root,n,0);
    sort(v.rbegin(),v.rend());
   // cout<<v[k1-1]<<endl;
    k1=v[k1-1];
    v.clear();
     if(k1 == 0)
         k1=1;
     if(k1%2!=0)
         cout<<"Case #"<<i+1<<": "<<k1/2<<" "<<k1/2<<endl;
     else{
        cout<<"Case #"<<i+1<<": "<<k1/2<<" "<<k1/2-1<<endl;
       }

    } 
    
} 

