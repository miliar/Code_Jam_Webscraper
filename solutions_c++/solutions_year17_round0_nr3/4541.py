#include <bits/stdc++.h>
using namespace std;


void q_push(priority_queue<int>& qu, int val)

{

//val *= -1;

qu.push(val);

}

void q_pop(priority_queue<int>& qu)

{

qu.pop();

}

int q_top(priority_queue<int>& qu)

{

int val = qu.top();

//val *= -1;

return val;

}

int main()

{

int tetC;

cin >> tetC;

for(int cnt = 0; cnt < tetC; cnt++) {

int curVal , totP;

cin >> curVal >> totP;

priority_queue<int> q;

q_push(q, curVal);

for(int ct = 0; ct < totP - 1; ct++) {

int curMax = q_top(q);

q_pop(q);

int c8, c9;

c8 = c9 = curMax / 2;

if(curMax % 2 == 0)

c9--;

q_push(q,c8);

q_push(q, c9);

}

int retVal = q_top(q);

int c8, c9;

c8 = c9 = retVal / 2;

if(retVal % 2 == 0)

c9--;
cout << "Case #"<<cnt+1<<": " << c8 << " " << c9 << endl;

}

return 0;

}

/////////////////////////////
