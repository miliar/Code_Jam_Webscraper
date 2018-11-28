#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/mman.h>

using namespace std;

#define VNAME(x) #x

const int INPUT_MAXSIZE = 3;
const int PAGE_SHIFT = 12;
const char* PRECISION = "%.7f";
const char* LINE = "%d %d\n";
const char* HEADER = "Case #%d: ";

typedef struct {
  int position;
  int speed;
} pair;

typedef struct {
  int length;
  int size;
  pair* data;
} testCase;

static inline int pagesize() {
  return INPUT_MAXSIZE*(1 << PAGE_SHIFT);
}

static inline int getmemflags() {
  return MAP_ANONYMOUS|MAP_PRIVATE|MAP_NORESERVE|MAP_LOCKED;
}

static inline int parseInteger() {
  static int res = 0;
  scanf("%d", &res);
  return res;
}

static inline void showInteger(int value) {
  printf("%d", value);
}

static inline void showDouble(double value, const char* format) {
  printf(format, value);
}

static inline void parseNewline() {
  scanf("\n");
}

static inline void showNewline() {
  printf("\n");
}

static inline pair* allocateBuffer() { 
  void* result = mmap(NULL, pagesize(), PROT_READ|PROT_WRITE, getmemflags(), -1, 0);
  if(result == MAP_FAILED) {
    printf(VNAME(MAP_FAILED));
    showNewline();
    _exit(EXIT_FAILURE);
  }
  return (pair*)result;
}

static inline void parseData(pair* data, int size) {
  for(int i=0; i<size; ++i) {
    scanf(LINE, &data[i].position, &data[i].speed);
  }
}

static inline const testCase* parseInput() {
  static testCase const testBuffer = {
    .length = 0,
    .size = 0,
    .data = allocateBuffer()
  };
  scanf(LINE, &testBuffer.length, &testBuffer.size);
  parseData(testBuffer.data, testBuffer.size);
  return &testBuffer;
}

static inline void showHeader(int testCaseId) {
  printf(HEADER, testCaseId); 
}

static inline double findMaxValue(const pair* last, int length) {
  double time = ((double)(length-last->position))/((double)last->speed);
  return ((double)length)/time;
}

static inline bool check(const pair* previous, const pair* next, int length) {   
  return ((long long)(length-next->position))*(long long)previous->speed >= ((long long)(length-previous->position))*(long long)next->speed;
}

static inline double process(const testCase* buffer) {
  static pair tmp = {
    .position = 0,
    .speed = 0
  };    
  tmp = buffer->data[0];  
  for(int i=1; i<buffer->size; ++i) {
    if(check(&tmp, &(buffer->data[i]), buffer->length)) {
      tmp = buffer->data[i];
    }
    else {
      break;
    }
  }  
  return findMaxValue(&tmp, buffer->length);
}

static inline void execute() {
  const testCase* inputBuffer = parseInput();
  double result = process(inputBuffer);
  showDouble(result, PRECISION);
}

static inline int run(int tests) {
  parseNewline();
  for(int i=1; i<=tests; ++i) {
    showHeader(i);
    execute();
    showNewline();
  }
  return EXIT_SUCCESS;
}

int main() {
  int amount = parseInteger();
  return run(amount);
}
