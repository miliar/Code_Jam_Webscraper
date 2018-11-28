#include<bits/stdc++.h>
using namespace std;
struct node
{
    int value,left,right;
};
node arr[100001];
void computeLeftandRight(int n,int index)
{
    int left_count,right_count;
    left_count=right_count=0;
    int i;
    i=index;
    i--;
    while(i>=0 && arr[i].value==-1)
    {
        i--;
        left_count++;
    }
    i=index;
    i++;
    while(i<n && arr[i].value==-1)
    {
        i++;
        right_count++;
    }
    arr[index].left=left_count;
    arr[index].right=right_count;
}
int compute(int n)
{
 vector<int>store_vector;
    for(int i=0;i<n;i++)
    {
        if(arr[i].value==-1)
        {
            computeLeftandRight(n,i);
            store_vector.push_back(i);
        }
    }
int local_min,local_max;
local_max=INT_MIN;
local_min=INT_MIN;
int answer;
for(auto it=store_vector.begin();it!=store_vector.end();it++)
{
    int i=(*it);
    if(min(arr[i].left,arr[i].right)>local_min)
    {
        local_min=min(arr[i].left,arr[i].right);
        local_max=max(arr[i].left,arr[i].right);
        answer=i;
    }
    else if(min(arr[i].left,arr[i].right)==local_min)
    {
        if(max(arr[i].left,arr[i].right)>local_max)
        {
            local_max=max(arr[i].left,arr[i].right);
            answer=i;
        }
    }

}
arr[answer].value=1;
return answer;
}
int main()
{
    int t,n,k;
    ifstream in_file;
    in_file.open("input.in");
    ofstream out_file;
    out_file.open("out.in");
    int test_case=1;
    in_file>>t;
    while(t--)
    {
        in_file>>n>>k;
        for(int i=0;i<n;i++)
        {
            arr[i].value=arr[i].left=arr[i].right=-1;
        }
        int min_answer,max_answer,final_answer;
        for(int i=1;i<=k;i++)
        {
          final_answer=compute(n);
          min_answer=min(arr[final_answer].left,arr[final_answer].right);
          max_answer=max(arr[final_answer].left,arr[final_answer].right);
          //cout<<final_answer<<" "<<min_answer<<" "<<max_answer<<endl;
        }
        out_file<<"Case #"<<test_case<<": "<<max_answer<<" "<<min_answer<<"\n";
        test_case++;
    }
    in_file.close();
    out_file.close();
    return 0;
}
