#include <iostream>
#include <algorithm>
using namespace std;

struct node{
	char ch;
	node* next;
};

node* crtNode(char ch1){
	node* tmp = new node;
	tmp->next = tmp;
	tmp->ch = ch1;
	return tmp;
}

node* initInsert(char ch,int n){
node* head = NULL;
node* tmp;
head = crtNode(ch);
n--;
while(n--){
tmp = crtNode(ch);
tmp->next = head->next;
head->next = tmp;
}

return head;
}

void findInsert(char ch,char ch1,char ch2,int n1,int n2,node* head){
node *prev,*tmp,*tmp1;
prev = head;
tmp = head->next;

while(n1--){
	while(tmp->ch != ch){
		prev = tmp;
		tmp = tmp->next;
	}
	tmp1 = crtNode(ch1);
	tmp1->next = tmp;
	prev->next = tmp1;
	prev = tmp;
	tmp = tmp->next;
}

while(n2--){
	while(tmp->ch != ch){
		prev = tmp;
		tmp = tmp->next;
	}
	tmp1 = crtNode(ch2);
	tmp1->next = tmp;
	prev->next = tmp1;
	prev = tmp;
	tmp = tmp->next;
}
} //end of fun.

void printList(node* head){
node* tmp = head->next;
while(tmp != head){
	cout << tmp->ch;
	tmp = tmp->next;
}
cout << tmp->ch;
cout << endl;
}//end of func.

bool Stable(node* head){
node* tmp = head->next;

while(tmp!=head){
	if(tmp->ch != tmp->next->ch)
		tmp = tmp->next;
	else
		return false;
}
return true;
}//end of func.

void deleteList(node* head){
node* tmp = head->next;
node* tmp1;
while(tmp!=head){
tmp1 = tmp;
tmp = tmp->next;
delete tmp1;
}
delete tmp;
}//end of func.

int main()
{
    int t,i,c=0;
    int n,r,o,y,g,v,b;
    int max;
    node *head;
    cin >> t;

    while(t--){
      head = NULL;
      c++;
      cin >> n >> r >> o >> y >> g >> b >> v;
      
      max = ((r>y && r>b)?r:((y>b)?y:b));
      
      if(max==r){
      	   head = initInsert('R',r);
      	   //printList(head);
           findInsert('R','Y','B',y,b,head);
         } //end of r max

        else if(max == y){
            head = initInsert('Y',y);
            //printList(head);
            findInsert('Y','R','B',r,b,head);
        }//end of y max;
        else{
        	head = initInsert('B',b);
        	//printList(head);
        	findInsert('B','Y','R',y,r,head);
        }
        cout << "Case #" << c <<": ";
        if(!Stable(head))
        	cout << "IMPOSSIBLE" << endl;
        else
        printList(head);
        deleteList(head);
      } //end of test case

	return 0;
}