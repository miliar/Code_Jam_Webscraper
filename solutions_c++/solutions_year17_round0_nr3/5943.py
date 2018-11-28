#include<iostream>
#include<cstdio>
#include<math.h>
using namespace std;

struct node {
	unsigned long long int val;
	unsigned long long int ref;
	node* next;
	node* previous;
};

class queue {
	public:
		node* head;
		node* tail;
		queue() {
			head = NULL;
			tail = NULL;
		}

		void enqueue(unsigned long long int val){
			node* new_node = (node*) malloc(sizeof(node));
			new_node->val = val;
			new_node->next = NULL;
			new_node->previous = NULL;
			new_node->ref = 0;

			if(tail == NULL) {
				tail = new_node;
				head = tail;
			} else {
				tail->next = new_node;
				tail = tail->next;
			}

		}

		void enqueue_sorted(unsigned long long int val) {
			node* new_node = (node*) malloc(sizeof(node));
			new_node->val = val;
			new_node->next = NULL;
			new_node->previous = NULL;
			new_node->ref = 1;

			if(head==NULL)
			{
				head = new_node;
				tail = head;
				return;
			}

			if(val < tail->val)
			{
				//if(val==4) cout<<"yog1 ";
				tail->next = new_node;
				new_node->previous = tail;
				tail = new_node;
				return;
			}
			if(val == tail->val) 
			{
				tail->ref++;
				return;
			}

			if(val > head->val) {
								//if(val==4) cout<<"yog3 ";

				new_node->next=head;
				head->previous = new_node;
				head = new_node;
				return;


			}

			if(val == head->val) {
				head->ref++;
				return;
			}


			if(head == tail)
			{
								//if(val==4) cout<<"yog2 ";

				new_node->next=head;
				head->previous = new_node;
				head = new_node;
				return;
			}


			

			node* p = tail->previous;
			node* prev = tail;


			while(p!=NULL)
			{
								//if(val==4) cout<<"yog4 ";

				if(val <= p->val)
				{
					if(val<p->val)
					{
						prev->previous = new_node;
						new_node->previous = p;
						new_node->next=prev;
						p->next=new_node;

						return;
					}
					else
					{
						p->ref++;
						return;
					}

				}
				prev = p;
				p = p->previous;
			}

		}

		void printQueue()
		{
			node* p = head;
			while(p!=NULL)
			{
				cout<<p->val<<" ";
				p = p->next;
			}
			cout<<endl;
		}

		unsigned long long int dequeue() {

			if(head->ref>1) {
				head->ref--;
				return head->val;
			}

			node* return_this = head;

			head = head->next;

			if(head == NULL) {
				tail = NULL;
			}
			unsigned long long int ret_val = return_this->val;
			free(return_this);
			return ret_val;
		}

		void purge_queue()
		{
			while(head!=NULL)
			{
				node* free_this = head;
				head = head->next;
				free(free_this);
			}
			tail = NULL;
		}
};

int main()
{
	int T;
	cin >>T;
	for(int i=0; i<T; i++)
	{
		queue Q;
		unsigned long long int S;
		unsigned long long int K;
		cin>>S;
		cin>>K;

		unsigned long long int s1=S;
		unsigned long long int k1=K;

		Q.enqueue_sorted(s1);
			//cout<<s1<<k1;
		node* fifo;
		unsigned long long int fifo_val;

		fifo_val = Q.dequeue();
		while(k1 > 1)
		{
			//cout<<fifo_val<<endl;
			if((fifo_val)%2==0)
			{
				fifo_val/=2;
				Q.enqueue_sorted(fifo_val);
				if(fifo_val!=0)
					Q.enqueue_sorted(fifo_val-1);
				else Q.enqueue_sorted(fifo_val);
			}
			else
			{
				fifo_val/=2;
				Q.enqueue_sorted(fifo_val);
				Q.enqueue_sorted(fifo_val);

			}
			//Q.printQueue();
			fifo_val=Q.dequeue();
			k1--;
		}
		//cout<<"YOG=fifoval="<<fifo_val<<endl;
		cout<<"Case #"<<i+1<<": ";
		if((fifo_val)%2==0)
		{
			//cout<<"enter here"<<endl;
			fifo_val/=2;
			cout<<fifo_val<<" ";
			if(fifo_val!=0)
				cout<<fifo_val-1;
			else cout<<fifo_val;
		}
		else
		{
			fifo_val/=2;
			cout<<fifo_val<<" ";
			cout<<fifo_val;
		}
		cout<<endl;

		Q.purge_queue();
		

	}
}





