#include <iostream>
#include <string>
#include <queue>
using namespace std;

struct tree
{
    struct tree* left;
    struct tree * right;
    int num;
};

tree* construct_tree(int N)
{
    if(N<=0)
        return NULL;
    tree * root = new tree;
    root->num = N;
    root->right = construct_tree((N-1)/2);
    root->left = construct_tree((N)/2);
    return root;
}
int main()
{
    int ttt;
    cin>>ttt;
    
    for(int tttt = 1;tttt<=ttt;tttt++)
    {
        cout<<"Case #"<<tttt<<": ";
        int N,x;
        cin>>N>>x;
        int l=(N)/2,lc = 1, r = (N-1)/2, rc = 1;
        
        if(x == 1)
        {
            cout<<l<<" "<<r<<endl;
        }
        else
        {
            x--;
            
            while(l!=0 && r!=0 && x!=1 && x > lc + rc)
            {
                x = x - lc -rc;
                int l1 = (l-1)/2;
                int l1c = lc;
                int l2  = (l)/2;
                int l2c = lc;
                int r1 = (r-1)/2;
                int r1c = rc;
                int r2 = r/2;
                int r2c = rc;
                l = l1;
                lc = l1c;
                rc = 0;
                if(l1 == l2)
                {
                    lc = lc +l2c;
                }
                else
                {
                    r = l2;
                    rc = rc+ l2c;
                }
            
                if(l1 == r1)
                {
                    lc = lc +r1c;
                }
                else
                {
                    r = r1;
                    rc = rc + r1c;
                }
                if(l1 == r2)
                {
                    lc = lc +r2c;
                }
                else
                {
                    r = r2;
                    rc = rc + r2c;
                }
            
                if(rc == 0)
                {
                    rc = lc/2;
                    r = l;
                    lc  = lc/2;
                }
                if(l<r)
                {
                    swap(l,r);
                    swap(lc,rc);
                }
               // printf("X : %d L: %d LC: %d, R: %d, RC: %d\n",x,l,lc,r,rc);
            }
            if(x <= lc )
                cout<<l/2<<" "<<max(0,(l-1)/2)<<endl;
            else
                cout<<r/2<<" "<<max(0,(r-1)/2)<<endl;
            
        }
        
    }
}
