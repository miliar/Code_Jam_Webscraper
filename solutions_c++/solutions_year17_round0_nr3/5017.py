#include <iostream>
#include<fstream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    ofstream cout;
    cout.open ("example.txt");
    ifstream cin;
    cin.open("input.txt");
    int test;
    cin >> test;
    int caseCounter=0;
    while (test--)
    {
        caseCounter++;
        int n,k;
        cin>>n>>k;
        priority_queue<int> pq;
        pq.push(n);
        for(int i = 0; i< k - 1 ; i++)
        {
            if(pq.empty())
            {
                break;
            }
            int current = pq.top();
            pq.pop();
            int right = (current - 1)/2;
            int left = current - 1 - right;
            if(right != 0)
            {
                pq.push(right);
            }
            if(left != 0)
            {
                pq.push(left);
            }
        }



        cout<<"Case #"<<caseCounter<<": ";
        if(pq.empty())
        {
            cout<<"0 0"<<endl;
        }
        else
        {
        int current = pq.top();
            pq.pop();
            int right = (current - 1)/2;
            int left = current - 1 - right;
            cout<<max(right, left)<<" "<<min(right, left)<<endl;
        }


    }
    cout.close();
    return 0;
}
