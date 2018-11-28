#include <bits/stdc++.h>

#define vi vector<int>
#define vb vector<bool>
#define ii pair<int, int>

using namespace std;

vector<vi> graph;

void printVec(vi a);
void printVec(vector<bool> a);
void printArr(int a[], int n);
void printArr(bool a[], int n);

int main()
{
    int t,m;
    cin >> t;
    for(m=1;m<=t;m++)
    {
        int n,i,j;
        string s, ans;
        cin >> s;
        ans.assign(s.begin(), s.end());
        n = s.size();
        int pos = -1;
        for(i=0;i<n-1;i++)
        {
            if(s[i] > s[i+1])
            {
                pos = i;
                break;
            }
            ans[i] = s[i];
        }
        if(pos == -1)
            ans[i] = s[i];
        else
        {
            for(i=pos;i>0;i--)
            {
                if(s[i-1] != s[pos])
                    break;
            }
            ans[i] = s[pos]-1;
            for(j=i+1;j<n;j++)
                ans[j] = '9';
        }
        if(ans[0] == '0')
            ans = ans.substr(1,ans.size());
        cout << "Case #" << m << ": " << ans << endl;
    }
    return 0;
}

void printVec(vi a)
{
    vi::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}

void printVec(vector<bool> a)
{
    vector<bool>::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}


void printArr(int a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}

void printArr(bool a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}