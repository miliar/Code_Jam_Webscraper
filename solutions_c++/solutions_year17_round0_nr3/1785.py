#include<iostream>
#include<list>
using namespace std;

struct node{
  long long int data;
  long long int freq;
};

int main()
{
  int n;
  cin>>n;
  for(int k=0;k<n;k++)
  {
    long long int num,people;
    cin>>num>>people;
    list<node> l;
    node newnode = {num,1};
    l.push_back(newnode);
    long long int left=0,right=0;
    while(people > 0)
    {
      bool rightInserted = 0,leftInserted = 0;

      //cout<<l.front().data<<":"<<l.front().freq<<endl;

      right = (l.front().data)/2;
      if(right<=0)
        rightInserted=1;
      long long int rightfreq = l.front().freq;

      left = right;
      if((l.front().data)%2==0)
        left --;
      if(left<=0)
        leftInserted=1;
      long long int leftfreq = l.front().freq;

      if(l.front().freq >= people)
          break;
      people -= l.front().freq;

      for(list<node>::iterator i = l.begin();i!=l.end() && (!leftInserted || !rightInserted);i++)
      {
        if((*i).data == right)
        {
          (*i).freq += rightfreq;
          rightInserted = 1;
        }
        if((*i).data == left)
        {
           (*i).freq += leftfreq;
           leftInserted = 1;
        }
      }

      if(!rightInserted)
      {
        if(left == right)
        {
          rightfreq *= 2;
          leftInserted = 1;
        }
        node newnode = {right,rightfreq};
        l.push_back(newnode);
      }
      if(!leftInserted)
      {
        node newnode = {left,leftfreq};
        l.push_back(newnode);
      }
      l.pop_front();
      }
      cout<<"case "<<"#"<<k+1<<": "<<right<<" "<<left<<endl;
  }
  return 0;
}
