#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/mman.h>

using namespace std;

#define VNAME(x) #x

const int IMPOSSIBLE = -1;
const int PAGE_SHIFT = 12;
const int INPUT_MAXSIZE = 1;
const char MINUS = '-';
const char PLUS = '+';
const int MINUS_VALUE = -1;
const int PLUS_VALUE = 1;
const char* LINE = "%s %d\n";
const char* HEADER = "Case #%d: ";

typedef struct {
  int offset;
  char* input;
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

static inline void parseNewline() {
  scanf("\n");
}

static inline void showNewline() {
  printf("\n");
}

static inline char* allocateBuffer() { 
  void* result = mmap(NULL, pagesize(), PROT_READ|PROT_WRITE, getmemflags(), -1, 0);
  if(result == MAP_FAILED) {
    printf(VNAME(MAP_FAILED));
    showNewline();
    _exit(EXIT_FAILURE);
  }
  return (char*)result;
}

static inline const testCase* parseLine() {
  static testCase const testBuffer = {
    .offset = 0,
    .input = allocateBuffer()
  };
  scanf(LINE, testBuffer.input, &testBuffer.offset);
  return &testBuffer;
}

static inline void showHeader(int testCaseId) {
  printf(HEADER, testCaseId); 
}

static inline int getValue(const char* input, int position) {
  int value = PLUS_VALUE;
  if(position >= 0 && input[position] == MINUS) {
    value = MINUS_VALUE;
  }
  return value;
}

static inline int process(const char* input, int length, int size) {  
  static char* const buffer = allocateBuffer();
  int result = 0;
  int bufferValue = PLUS_VALUE;
  for(int i=0; i<length; ++i) {    
    if(getValue(input, i)*bufferValue == MINUS_VALUE) {      
      if(i+size-1 < length) {
	++result;
	buffer[i] = MINUS;
      }
      else {
	result = IMPOSSIBLE;
	break;
      }
    }
    else {
      buffer[i] = PLUS;      
    }
    bufferValue *= getValue(buffer, i)*getValue(buffer, i-size+1);
  }  
  return result;
}

static inline void showResult(int res) {
  if(res == IMPOSSIBLE) {
    printf(VNAME(IMPOSSIBLE));
  }
  else {
    showInteger(res);
  }
}

static inline void execute() {
  const testCase* inputBuffer = parseLine();
  int result = process(inputBuffer->input, strlen(inputBuffer->input), inputBuffer->offset);
  showResult(result);
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
