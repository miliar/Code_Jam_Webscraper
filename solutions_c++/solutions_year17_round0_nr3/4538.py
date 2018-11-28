#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <string>
using namespace std;

int s2n(string input)
{
    int out=0;
    int neg=1;
    if (input.length()>=1)
    {
        if (input[0]=='-')
        {
            neg=-1;
            input=input.substr(1,input.length()-1);
        }
    }
    for (int i=0;i<input.length();i++)
    {
        out*=10;
        out+=input[i]-'0';
    }
    out*=neg;
    return out;
}

struct stallTreeNode{
    int size, l, r, index;
    stallTreeNode* parent;
    stallTreeNode* left;
    stallTreeNode* right;
};

int main(void)
{
    ifstream ifile;
    ofstream ofile;
    ofile.open("stallOUT.txt");
    ifile.open("stall.in");
    string input="";
    getline(ifile,input);
    int sets = s2n(input);
//    sets = 1;
    for (int set=0;set<sets;set++)
    {
        ofile<<"Case #"<<set+1<<": ";
        cout<<"Case #"<<set+1<<": ";
        getline(ifile,input);
        string::size_type pos;
        pos=input.find(' ',0);
        int n = s2n(input.substr(0,pos));
        int k = s2n(input.substr(pos+1));
        if (k==n){
            ofile<<"0 0"<<endl;
            cout<<"0 0"<<endl;
            continue;
        }
        stallTreeNode* bathroom = new stallTreeNode; bathroom->size=n; bathroom->l=1; bathroom->r=n; bathroom->index = -1; bathroom->parent=NULL;
        stallTreeNode* last;
        for (int i=0;i<k;i++){
            stallTreeNode* traverse = bathroom;
            while (traverse->index!=-1){
//                cout<<traverse->left->size<<" "<<traverse->right->size<<endl;
                traverse = traverse->left->size >= traverse->right->size ? traverse->left : traverse->right;
            }
            traverse->index = (traverse->l + traverse->r)/2;
//            cout<<traverse->index<<endl;
//            cout<<endl<<traverse->size<<" "<<traverse->l<<" "<<traverse->index<<" "<<traverse->r<<endl<<endl;
            
            stallTreeNode* lhs = new stallTreeNode;
            lhs->index=-1; lhs->size=traverse->index-traverse->l; lhs->l=traverse->l; lhs->r=traverse->index-1;
            lhs->parent=traverse;
            
            stallTreeNode* rhs = new stallTreeNode;
            rhs->index=-1; rhs->size=traverse->r-traverse->index; rhs->l=traverse->index+1; rhs->r=traverse->r;
            rhs->parent=traverse;
            
            traverse->left = lhs; traverse->right = rhs;
            last = traverse;
            int max = lhs->size>rhs->size ? lhs->size : rhs->size;
            traverse->size = max;
            while (traverse->parent!=NULL){
                max = traverse->left->size>traverse->right->size ? traverse->left->size : traverse->right->size;
                traverse->size = max;
                traverse=traverse->parent;
            }
        }
        int min = last->left->size < last->right->size ? last->left->size : last->right->size;
        int max = last->left->size > last->right->size ? last->left->size : last->right->size;
        ofile<<max<<" "<<min<<endl;
        cout<<max<<" "<<min<<endl;
    }
    ofile.close();
    return 0;
}































